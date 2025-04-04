```markdown
# theme_adaptable - Documentación del Plugin

## 1. Descripción general

El tema `theme_adaptable` es un tema para Moodle diseñado para ofrecer una experiencia de usuario moderna y flexible. Se centra en la adaptabilidad a diferentes dispositivos y en la personalización para adaptarse a las necesidades específicas de cada institución educativa. Este tema proporciona una base sólida para construir un entorno de aprendizaje online atractivo y funcional.

`theme_adaptable` se basa en el tema Boost de Moodle y extiende sus capacidades. Esto significa que aprovecha la robustez y las características centrales de Boost mientras añade opciones de personalización adicionales y mejoras en la interfaz.

Este documento tiene como objetivo guiar a los administradores de Moodle en la instalación, configuración y uso del tema `theme_adaptable`.

## 2. Funcionalidades principales

*   **Diseño Responsivo:** Adaptabilidad total a diferentes tamaños de pantalla, incluyendo ordenadores de escritorio, tablets y smartphones, garantizando una experiencia consistente en todos los dispositivos.
*   **Personalización de Colores:** Permite modificar los colores principales del tema para alinearlos con la identidad visual de la institución.
*   **Personalización del Logotipo:** Facilita la carga del logotipo de la institución para una marca consistente en toda la plataforma Moodle.
*   **Personalización del Pie de Página:**  Permite personalizar el contenido del pie de página, incluyendo enlaces importantes, información de contacto, y avisos legales.
*   **Menú de Navegación Personalizable:** Facilita la creación de un menú de navegación principal intuitivo y adaptable a las necesidades de la institución. (Dependiendo de la versión del tema)
*   **Integración con Bloques:** Permite la utilización y configuración de bloques estándar de Moodle para añadir funcionalidades y contenido adicional a las páginas del curso.
*   **Compatibilidad con Boost:** Basado en el tema Boost, por lo que es compatible con sus funcionalidades y configuraciones.

**Nota:** La disponibilidad de funciones específicas puede variar dependiendo de la versión exacta del tema `theme_adaptable`.  Es recomendable consultar la documentación específica de la versión que esté utilizando.

## 3. Cómo instalar y configurar el plugin

### Instalación

1.  **Descarga:** Descarga el paquete del tema `theme_adaptable` desde el repositorio de Moodle plugins o desde el sitio web del desarrollador (ver sección Enlaces Útiles). Asegúrate de descargar la versión compatible con tu versión de Moodle.
2.  **Subida del Archivo:** Accede a tu sitio Moodle con una cuenta de administrador. Navega a *Administración del sitio > Extensiones > Instalar extensiones*.
3.  **Instalación:**
    *   Arrastra y suelta el archivo ZIP del tema en el área designada en la página de instalación.
    *   Alternativamente, haz clic en el botón "Seleccionar un archivo..." para buscar y cargar el archivo ZIP desde tu ordenador.
4.  **Continuar:**  Moodle detectará el tema e iniciará el proceso de instalación. Revisa las comprobaciones y haz clic en "Continuar".
5.  **Actualizar la base de datos:** Sigue las instrucciones en pantalla para actualizar la base de datos de Moodle.
6.  **Configuración del tema:** Una vez finalizada la instalación, es recomendable revisar las opciones de configuración del tema (paso siguiente).

### Configuración

1.  **Selección del tema:** Ve a *Administración del sitio > Apariencia > Selector de temas*.
2.  **Selecciona el tema Adaptable:**  Haz clic en el botón "Usar tema" junto al tema `Adaptable`.
3.  **Configuración del tema:** Ve a *Administración del sitio > Apariencia > Ajustes del tema > Adaptable*.
4.  **Personalización:**  En la página de configuración del tema, encontrarás varias opciones para personalizar la apariencia de tu sitio Moodle:
    *   **Ajustes generales:** Permite configurar el logotipo, el esquema de color, la tipografía, entre otros.
    *   **Ajustes de encabezado:** Permite personalizar el encabezado de la página, incluyendo el menú de navegación y el banner principal.
    *   **Ajustes de pie de página:** Permite personalizar el pie de página, incluyendo la información de contacto y los enlaces importantes.
    *   **Otras secciones:** Dependiendo de la versión del tema, es posible que encuentres opciones adicionales para personalizar la barra lateral, los bloques y otras áreas de la página.

5.  **Guardar Cambios:** Una vez que hayas configurado las opciones deseadas, haz clic en el botón "Guardar cambios" en la parte inferior de la página.

**Importante:**  Después de realizar cambios en la configuración del tema, es recomendable vaciar la caché del tema y del navegador para asegurarte de que los cambios se visualicen correctamente. Puedes vaciar la caché del tema en *Administración del sitio > Apariencia > Temas > Selector de temas > Limpiar caché de temas*.

## 4. Preguntas frecuentes (FAQ)

*   **¿Es `theme_adaptable` compatible con mi versión de Moodle?**
    *   Verifica la compatibilidad en la página del plugin en el repositorio de Moodle plugins o en la documentación oficial del tema.
*   **¿Cómo puedo cambiar el logotipo de mi sitio?**
    *   Ve a *Administración del sitio > Apariencia > Ajustes del tema > Adaptable > Ajustes generales*. Busca la opción para cargar el logotipo.
*   **¿Cómo puedo cambiar los colores del tema?**
    *   Ve a *Administración del sitio > Apariencia > Ajustes del tema > Adaptable > Ajustes generales*. Busca las opciones para modificar los colores principales del tema.
*   **¿Puedo personalizar el pie de página?**
    *   Sí, ve a *Administración del sitio > Apariencia > Ajustes del tema > Adaptable > Ajustes de pie de página*.
*   **¿El tema `theme_adaptable` afecta el rendimiento de mi sitio Moodle?**
    *   Como cualquier tema, `theme_adaptable` puede afectar el rendimiento.  Optimizar las imágenes del logo y otros recursos visuales puede ayudar a mejorar la velocidad de carga. Considera habilitar la caché de Moodle para mejorar el rendimiento general.

## 5. Problemas comunes y soluciones

*   **El tema no se muestra correctamente después de la instalación:**
    *   Asegúrate de haber vaciado la caché del tema y del navegador.
    *   Verifica que el tema esté activado como el tema predeterminado en el selector de temas.
    *   Verifica si hay errores en los registros del servidor o en la consola del navegador.
*   **Los cambios en la configuración del tema no se reflejan:**
    *   Vuelve a vaciar la caché del tema y del navegador.
    *   Asegúrate de haber guardado los cambios en la configuración del tema.
    *   Si utilizas un CDN, es posible que debas purgar la caché del CDN.
*   **Errores de Javascript o CSS:**
    *   Verifica si hay errores de Javascript o CSS en la consola del navegador. Estos errores pueden impedir que el tema funcione correctamente. Intenta desactivar plugins de terceros uno por uno para identificar conflictos.
*   **Incompatibilidad con plugins:**
    *   Algunos plugins pueden no ser totalmente compatibles con `theme_adaptable`.  Si encuentras problemas, contacta al desarrollador del plugin o considera usar un plugin alternativo.

## 6. Enlaces útiles

*   **Repositorio de Moodle Plugins:**  https://moodle.org/plugins/theme_adaptable
*   **GitHub (si el plugin es de código abierto):** https://github.com/gjbarnard/moodle-theme_adaptable
*   **Documentación Oficial:** https://moodle.org/plugins/theme_adaptable

**Nota:** Es crucial consultar la documentación oficial del tema y el repositorio de código (si es de código abierto) para obtener información específica sobre la versión que estás utilizando y para mantenerte actualizado sobre las últimas características, correcciones de errores y actualizaciones de seguridad.
```
