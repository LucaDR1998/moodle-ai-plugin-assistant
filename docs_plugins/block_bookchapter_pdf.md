```markdown
# Documentación del Plugin 'block_bookchapter_pdf' para Moodle

## 1. Descripción general

El plugin 'block_bookchapter_pdf' para Moodle es un bloque diseñado para facilitar el acceso a archivos PDF directamente relacionados con un capítulo específico de un libro dentro del curso. Este bloque permite a los profesores enlazar archivos PDF a los capítulos de un libro en Moodle, proporcionando a los estudiantes una forma sencilla y directa de acceder a materiales de lectura complementarios, ejercicios, o versiones imprimibles del contenido.  El objetivo principal es mejorar la experiencia de aprendizaje, centralizando el acceso a recursos importantes dentro del contexto del capítulo del libro.

**Nota:** Este bloque *solo* funciona dentro de la vista de un capítulo de un libro.  No será visible en otras páginas del curso.

## 2. Funcionalidades principales

*   **Vinculación directa a archivos PDF:** Permite a los profesores subir o enlazar un archivo PDF específico para cada capítulo de un libro.
*   **Interfaz sencilla e intuitiva:** La configuración del bloque es simple, permitiendo añadir y gestionar los enlaces PDF de manera eficiente.
*   **Accesibilidad mejorada:** Facilita el acceso rápido y directo a los recursos PDF relevantes para cada capítulo del libro.
*   **Opciones de visibilidad:** (Si implementado) Permite controlar la visibilidad del enlace PDF a los estudiantes.

## 3. Cómo instalar y configurar el plugin

### Instalación

1.  **Descarga:** Descarga el paquete del plugin 'block_bookchapter_pdf' desde https://moodle.org/plugins/block_bookchapter_pdf.
2.  **Subida del plugin:**
    *   Inicia sesión en tu sitio Moodle como administrador.
    *   Navega a: *Administración del sitio > Plugins > Instalar plugins*.
    *   Sube el archivo ZIP del plugin (arrástralo y suéltalo o selecciona el archivo).
3.  **Instalación:**
    *   Moodle verificará el paquete del plugin.  Haz clic en "Instalar el plugin desde el archivo ZIP".
    *   Revisa la página de validación del plugin y haz clic en "Continuar".
    *   Revisa las dependencias y haz clic en "Continuar".
    *   Moodle instalará el plugin. Si se requiere, sigue las instrucciones para actualizar la base de datos.
4.  **Configuración (si es necesaria):**
    *   Después de la instalación, es posible que necesites configurar ajustes globales para el plugin.  Ve a *Administración del sitio > Plugins > Bloques > block_bookchapter_pdf* (o la ruta correspondiente) para acceder a las opciones de configuración.  Si no hay opciones de configuración, este paso no es necesario.

### Configuración dentro de un curso

1.  **Activar el modo edición:** En el curso donde quieres usar el bloque, activa el "Modo edición".
2.  **Añadir el bloque:** En la columna donde deseas que aparezca el bloque, haz clic en "Añadir un bloque" (generalmente en la parte inferior de la columna izquierda o derecha).
3.  **Selecciona el bloque 'block_bookchapter_pdf':**  En el menú desplegable, busca y selecciona "block_bookchapter_pdf".
4.  **Configuración del bloque (en la vista del capítulo):**
    *   Navega a un libro dentro de tu curso.
    *   Asegúrate de estar visualizando un **capítulo específico** del libro. *El bloque solo se mostrará en la vista de un capítulo.*
    *   En el bloque 'block_bookchapter_pdf', deberías ver una opción para configurar el archivo PDF asociado al capítulo.
    *   Haz clic en el icono de "Editar" (generalmente un engranaje o un lápiz).
    *   Subir o enlazar un archivo PDF: Utiliza el selector de archivos de Moodle para subir un archivo PDF desde tu ordenador o seleccionar uno existente en el repositorio de archivos de Moodle.
    *   Guarda la configuración.

## 4. Preguntas frecuentes (FAQ)

*   **¿Por qué no veo el bloque 'block_bookchapter_pdf' en mi curso?**
    *   Asegúrate de que el bloque está instalado correctamente (ver sección de Instalación).
    *   Verifica que el "Modo edición" está activado en el curso.
    *   Asegúrate de que estás visualizando un **capítulo específico** dentro de un libro. El bloque no aparecerá en la página principal del curso ni en otras actividades que no sean capítulos de libros.
*   **¿Puedo usar este bloque para enlazar otros tipos de archivos además de PDF?**
    *   No, este bloque está diseñado específicamente para archivos PDF.
*   **¿Cómo puedo cambiar el archivo PDF asociado a un capítulo?**
    *   Navega al capítulo del libro en cuestión.
    *   Haz clic en el icono de "Editar" en el bloque 'block_bookchapter_pdf'.
    *   Elimina el archivo existente y sube o enlaza el nuevo archivo PDF.
*   **¿Puedo añadir múltiples archivos PDF a un capítulo?**
    *   No.  Actualmente, este bloque soporta la vinculación de un único archivo PDF por capítulo.  Si necesitas vincular varios archivos, considera comprimirlos en un único archivo ZIP y subir este archivo.

## 5. Problemas comunes y soluciones

*   **El bloque no aparece incluso después de la instalación.**
    *   Asegúrate de haber completado todos los pasos de la instalación correctamente.
    *   Verifica que el plugin está activado en la administración del sitio ( *Administración del sitio > Plugins > Descripción general de plugins*).
    *   Limpia la caché de Moodle ( *Administración del sitio > Desarrollo > Purgar todas las cachés*).
*   **Error al subir el archivo PDF.**
    *   Verifica que el archivo PDF no exceda el límite de tamaño de archivo permitido por Moodle.  Este límite se puede configurar en *Administración del sitio > Seguridad > Políticas del sitio*.
    *   Asegúrate de que el archivo PDF no está dañado.
    *   Comprueba los permisos del directorio de archivos de Moodle.
*   **El enlace al PDF no funciona.**
    *   Verifica que el archivo PDF se haya subido correctamente al repositorio de archivos de Moodle.
    *   Comprueba que el enlace al archivo PDF es correcto en la configuración del bloque.
    *   Verifica que el usuario tiene los permisos necesarios para acceder al archivo PDF.

## 6. Enlaces útiles

*   **Documentación oficial del plugin:** https://moodle.org/plugins/block_bookchapter_pdf
*   **Repositorio de GitHub:** https://github.com/LucaDR1998/moodle-block_bookchapter_pdf/tree/main
*   **Documentación oficial de Moodle sobre bloques:** https://docs.moodle.org/405/en/Blocks
```
