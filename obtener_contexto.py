from pymilvus import connections, Collection
from sentence_transformers import SentenceTransformer
import constantes
import keys

COLLECTION_NAME = "plugin_docs"
EMBEDDING_DIM = 384 # dimensión del embedding (modelo MiniLM-L6-v2)
TOP_K = 3

# modelo embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

# conexión con MILVUS
connections.connect(
    uri=constantes.MILVUS_URI,
    token=keys.MILVUS_TOKEN
)

collection = Collection(COLLECTION_NAME)
collection.load()

# busqueda del contexto
def get_plugin_context(query: str, top_k=TOP_K):
    # transformo el texto en un vector de 384 dimensiones 
    query_vector = model.encode([query])[0].tolist()

    search_params = {
        "metric_type": "COSINE",
        "params": {"nprobe": 10} # numero de clusters a explorar
    }

    # busco los vectores más similares al query_vector en el campo embedding
    # devuelve hasta 3 resultados 
    # extraigo los campos "plugin" y "text" de los resultados
    results = collection.search(
        data=[query_vector],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["plugin", "text"]
    )

    # creo el contexto 
    context_chunks = []
    for result in results[0]:
        plugin = result.entity.get("plugin")
        text = result.entity.get("text")
        score = result.distance
        context_chunks.append(f"[{plugin}] {text}  (score: {score:.2f})") # score de similitud

    return "\n\n".join(context_chunks)
