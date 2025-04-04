```markdown
# Documentación del Plugin mod_customcert para Moodle

## 1. Descripción general

El plugin `mod_customcert` para Moodle permite a los administradores y profesores crear certificados personalizados para los participantes del curso.  Esta herramienta ofrece la flexibilidad de diseñar certificados que reflejen la identidad visual de la institución y que se adapten a las necesidades específicas de cada curso o actividad.  A diferencia de los certificados genéricos, `mod_customcert` permite la inclusión de elementos variables como nombres, fechas de finalización y el nombre del curso, lo que aumenta la credibilidad y valor percibido del certificado. El plugin ofrece diferentes plantillas predefinidas y la posibilidad de cargar imágenes de fondo y personalizar los campos de texto.
Actualmente, no todas las versiones de Moodle son compatibles con el plugin, por lo que es importante verificar la compatibilidad antes de la instalación.

## 2. Funcionalidades principales

El plugin `mod_customcert` ofrece las siguientes funcionalidades:

*   **Creación de certificados personalizados:** Permite diseñar certificados únicos para cada curso o actividad.
*   **Plantillas predefinidas:**  Proporciona plantillas de certificado para comenzar rápidamente, las cuales se pueden personalizar.
*   **Campos dinámicos:** Admite la inclusión de campos variables como:
    *   Nombre del usuario
    *   Fecha de finalización del curso
    *   Nombre del curso
    *   Códigos de identificación únicos
*   **Carga de imágenes de fondo:** Permite utilizar imágenes personalizadas como fondo del certificado.
*   **Personalización de texto:** Permite cambiar la fuente, el tamaño y el color del texto.
*   **Descarga en formato PDF:** Genera el certificado en formato PDF para facilitar su impresión y distribución.
*   **Restricciones de acceso:** Permite definir criterios para otorgar el certificado (por ejemplo, completar todas las actividades del curso, obtener una calificación mínima).
*   **Compatibilidad:** El plugin es compatible con versiones específicas de Moodle. Verificar la compatibilidad antes de la instalación.

## 3. Cómo instalar y configurar el plugin

**Instalación:**

1.  **Descarga:** Descargue el archivo ZIP del plugin `mod_customcert` desde el repositorio oficial (ver sección Enlaces útiles).
2.  **Instalación a través de la interfaz web de Moodle:**
    *   Inicie sesión en Moodle como administrador.
    *   Vaya a Administración del sitio > Plugins > Instalar plugins.
    *   Arrastre y suelte el archivo ZIP del plugin o seleccione "Elegir un archivo".
    *   Haga clic en "Instalar plugin desde el archivo ZIP".
    *   Siga las instrucciones en pantalla.
3.  **Instalación manual (vía FTP/SSH):**
    *   Descomprima el archivo ZIP del plugin.
    *   Cargue la carpeta `customcert` a la carpeta `mod` en el directorio raíz de su instalación de Moodle (por ejemplo, `/var/www/moodle/mod/`).
    *   Inicie sesión en Moodle como administrador.
    *   Vaya a Administración del sitio > Notificaciones. Moodle detectará el nuevo plugin y lo instalará.

**Configuración:**

1.  **Configuración global:**
    *   Vaya a Administración del sitio > Plugins > Módulos de actividad > Certificado personalizado.
    *   Revise y configure las opciones globales.
    *   **Opciones importantes:**
        *   **Ruta a la librería TCPDF:** (Importante si no está instalado) Moodle debe poder acceder a la libreria TCPDF para la correcta generación de PDFs.
        *   **Habilitar debugging:** Habilita el logging para poder verificar el comportamiento del plugin.

2.  **Configuración a nivel de curso:**
    *   Activar el modo de edición en el curso.
    *   Haga clic en "Añadir una actividad o recurso".
    *   Seleccione "Certificado personalizado".
    *   Configure las opciones del certificado:
        *   **Nombre:** El nombre del certificado.
        *   **Plantilla:** Seleccione una plantilla predefinida o cree una nueva.
        *   **Fondo:** Cargue una imagen de fondo.
        *   **Campos:** Añada y configure los campos dinámicos (nombre del usuario, fecha, etc.).
        *   **Restricciones:** Defina los criterios para otorgar el certificado (si es necesario).
        *   **Opciones de descarga:** Formato, etc.

## 4. Preguntas frecuentes (FAQ)

*   **¿Puedo usar mis propias imágenes para el fondo del certificado?**
    Sí, puede cargar sus propias imágenes en formatos como JPG, PNG o GIF. Asegúrese de que la imagen tenga una resolución adecuada para evitar problemas de calidad al imprimir el certificado.

*   **¿Cómo puedo añadir un logo a mi certificado?**
    Puede insertar el logo como una imagen en el fondo del certificado.  Debe preparar la imagen con la posición donde desea mostrar el logo.

*   **¿Puedo personalizar el texto del certificado?**
    Sí, puede personalizar la fuente, el tamaño y el color del texto.

*   **¿Cómo puedo asegurarme de que los certificados se generen correctamente?**
    Asegúrese de que la librería TCPDF esté instalada y configurada correctamente en Moodle.  Además, verifique la configuración de permisos de archivo en el servidor. Si tiene problemas, habilite el "debugging" en la configuración global del plugin para obtener más información.

*   **¿El plugin es compatible con mi versión de Moodle?**
    Consulte la sección de compatibilidad en el repositorio oficial del plugin o en la página de descarga.  Es importante utilizar una versión compatible para evitar problemas.

## 5. Problemas comunes y soluciones

*   **Certificado no se genera correctamente:**
    *   **Solución:** Verifique que la librería TCPDF esté instalada y correctamente configurada en Moodle. Compruebe los permisos de archivo en el servidor. Habilite el debugging para obtener más información del error.
*   **Problemas con la visualización de caracteres especiales (acentos, etc.):**
    *   **Solución:** Asegúrese de que la codificación del texto del certificado sea UTF-8.  Además, seleccione una fuente que admita caracteres especiales.
*   **Imagen de fondo no se muestra correctamente:**
    *   **Solución:** Verifique que la ruta a la imagen sea correcta y que el archivo exista en el servidor.  Asegúrese de que el formato de la imagen sea compatible (JPG, PNG, GIF).
*   **El certificado no se otorga a pesar de cumplir las condiciones:**
    *   **Solución:** Verifique la configuración de las restricciones de acceso.  Asegúrese de que las condiciones estén correctamente definidas y que el usuario cumpla con todos los requisitos. Revisar las fechas de finalización del curso.
*   **Errores al instalar el plugin:**
    *   **Solución:** Asegúrese de que está instalando el plugin correctamente.  Verifique que la carpeta `customcert` esté en la carpeta `mod` de su instalación de Moodle. Revise los permisos de archivo.  Si el problema persiste, consulte los registros de errores de Moodle para obtener más información.

## 6. Enlaces útiles

*   **Documentación oficial del plugin (Moodle Plugins Directory):** https://moodle.org/plugins/mod_customcert
*   **Código fuente en GitHub (si está disponible públicamente):** https://github.com/mdjnelson/moodle-mod_customcert
* **Más documentación oficiál:** https://docs.moodle.org/405/en/Custom_certificate_module

**Nota:** La disponibilidad de la documentación oficial y el código fuente en GitHub puede variar. Consulte la página del plugin en el directorio de plugins de Moodle para obtener los enlaces más actualizados.
```
