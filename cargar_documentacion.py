import os
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from sentence_transformers import SentenceTransformer
import constantes
import keys

COLLECTION_NAME = "plugin_docs"
EMBEDDING_DIM = 384  # para el modelo all-MiniLM-L6-v2
model = SentenceTransformer("all-MiniLM-L6-v2")

# conexión a ZILLIZ CLOUD (Milvus SaaS)
connections.connect(
    uri=constantes.MILVUS_URI,        
    token=keys.MILVUS_TOKEN 
)

# si no existe creo la colleción
if not utility.has_collection(COLLECTION_NAME):
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="plugin", dtype=DataType.VARCHAR, max_length=100), # nombre plugin
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=2000), # trozo de documentación
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=EMBEDDING_DIM) # vector de texto
    ]
    schema = CollectionSchema(fields, description="Documentación plugin Moodle")
    collection = Collection(name=COLLECTION_NAME, schema=schema)
    print("# Colección creada")
else:
    collection = Collection(COLLECTION_NAME)

# partir el texto en trozos de 150 palabras
def chunk_text(text, max_words=150):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

# recupero los archivos .md que contienen la docuemnatción creada con Gemini
doc_dir = constantes.OUTPUT_DIR
files = [f for f in os.listdir(doc_dir) if f.endswith(".md")]
all_data = []

print(f"# Encontrados {len(files)} ficheros Markdown en {doc_dir}")

for file in files:
    # obtengo nombre del plugin
    plugin = file.replace(".md", "")
    with open(os.path.join(doc_dir, file), "r", encoding="utf-8") as f:
        content = f.read() # leo contenido
    # parto el contenido
    chunks = chunk_text(content)
    # cualculo el embedding de cada parte
    embeddings = model.encode(chunks).tolist()

    for chunk, emb in zip(chunks, embeddings):
        all_data.append({
            "plugin": plugin,
            "text": chunk,
            "embedding": emb
        })

print(f"# Generados {len(all_data)} chunk a indexar")

# insertar datos en MILVUS
insert_data = [
    [item["plugin"] for item in all_data],
    [item["text"] for item in all_data],
    [item["embedding"] for item in all_data]
]

collection.insert(insert_data)
collection.flush() # confirmar que todo se ha guardado

print("# Datos insertados")

# crear indice para busqueda
if not collection.has_index():
    index_params = {
        "metric_type": "COSINE", # cosine similarity es ideal para busqudas semanticas
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }
    collection.create_index(field_name="embedding", index_params=index_params)
    print("# Índice creado")

# cargo la colección
collection.load()
print("# Colección cargada en memoria")
print("# Documentación indexada en MILVUS")
