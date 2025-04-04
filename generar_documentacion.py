import os
import lib
import constantes

plugin_list = ["block_dedication", "mod_customcert", "block_bookchapter_pdf", "local_adminer", "theme_adaptable"]
os.makedirs(constantes.OUTPUT_DIR, exist_ok=True)

for plugin in plugin_list:
    print(f"# Generando documentación para: {plugin}...")

    prompt = f"""
Genera una documentación exhaustiva, clara y profesional en formato Markdown para el plugin de Moodle llamado '{plugin}'.

Incluye las siguientes secciones:

1. Descripción general  
2. Funcionalidades principales  
3. Cómo instalar y configurar el plugin  
4. Preguntas frecuentes (FAQ)  
5. Problemas comunes y soluciones  
6. Enlaces útiles (documentación oficiál del plugin y enlaces a github del mismo)

No inventes funcionalidades si no se conocen. El objetivo es informar al administrador de Moodle.
"""

    risposta = lib.call_gemini(prompt) 
    markdown = lib.extract_text_mkarkdown(risposta)

    if markdown:
        path = os.path.join(constantes.OUTPUT_DIR, f"{plugin}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"# Documentación guardada en: {path}")
    else:
        print(f"# No se pudo generar documentación para: {plugin}")

print("\n# Proceso completado")
