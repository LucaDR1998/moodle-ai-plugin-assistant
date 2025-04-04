```markdown
# Documentación del Plugin 'block_dedication' para Moodle

## 1. Descripción general

El plugin 'block_dedication' para Moodle es un bloque personalizable que permite mostrar mensajes de dedicación o agradecimiento a personas, organizaciones o instituciones dentro de un curso.  Este bloque es ideal para reconocer el esfuerzo y la contribución de quienes hacen posible la creación y el mantenimiento de un curso en Moodle.  El administrador del curso puede definir el título del bloque y el mensaje de dedicación, permitiendo una flexibilidad considerable en su uso. El bloque está diseñado para ser visualmente sencillo y fácil de configurar, proporcionando una manera rápida y efectiva de agregar reconocimiento dentro del entorno de aprendizaje.

## 2. Funcionalidades principales

*   **Título Personalizable:** Permite al administrador del curso definir el título del bloque, adaptándolo al contexto específico de la dedicación.
*   **Mensaje de Dedicación Personalizable:** Permite al administrador del curso escribir un mensaje de dedicación detallado, reconociendo a las personas u organizaciones que han contribuido.  Este mensaje puede incluir texto formateado básico (dependiendo del editor configurado en Moodle).
*   **Visibilidad Controlada:** El bloque, como cualquier otro bloque de Moodle, permite controlar su visibilidad a diferentes roles de usuario dentro del curso.
*   **Posicionamiento Flexible:** Permite ubicar el bloque en las diferentes regiones disponibles en la página del curso, según el tema de Moodle utilizado.
*   **Fácil Configuración:** La configuración del bloque es sencilla y directa, accesible a través de la interfaz de administración del curso.

## 3. Cómo instalar y configurar el plugin

**Instalación:**

1.  **Descarga el plugin:** Descarga el archivo comprimido `.zip` del plugin `block_dedication` desde la fuente oficial (generalmente el repositorio de plugins de Moodle o GitHub).
2.  **Accede a la administración de Moodle:** Inicia sesión en tu sitio Moodle con una cuenta de administrador.
3.  **Instala el plugin:**
    *   Ve a *Administración del sitio > Plugins > Instalar plugins*.
    *   Arrastra y suelta el archivo `.zip` en el área designada o usa el selector de archivos para encontrar el archivo.
    *   Haz clic en "Instalar plugin desde el archivo ZIP".
4.  **Revisa la información del plugin:** Moodle mostrará detalles sobre el plugin. Revisa la información y haz clic en "Continuar".
5.  **Confirma la instalación:** Revisa los requisitos y dependencias. Si todo es correcto, haz clic en "Actualizar base de datos ahora".
6.  **Configura el plugin (si es necesario):** Después de la actualización de la base de datos, es posible que Moodle te redirija a una página de configuración del plugin.  Si no, es posible que algunas opciones de configuración global se encuentren en *Administración del sitio > Plugins > Bloques > Dedication*.  Normalmente, este plugin no requiere configuración global.

**Configuración del bloque en un curso:**

1.  **Activa la edición en el curso:** Ve al curso donde deseas agregar el bloque y activa el modo edición haciendo clic en el botón "Activar edición" (generalmente en la esquina superior derecha).
2.  **Añade el bloque:** En la columna lateral o en la región de bloques (dependiendo del tema), busca el bloque "Añadir un bloque" y selecciona "Dedication" de la lista.
3.  **Configura el bloque:** Una vez que el bloque "Dedication" se ha añadido al curso, busca el icono de engranaje (⚙) en la barra de título del bloque y haz clic en él para acceder a su configuración.
4.  **Personaliza el título y el mensaje:** En la página de configuración del bloque, edita los campos "Título del bloque" y "Mensaje de dedicación" con el texto deseado.
5.  **Guarda los cambios:** Haz clic en el botón "Guardar cambios" al final de la página para aplicar la configuración.

## 4. Preguntas frecuentes (FAQ)

*   **¿Puedo usar HTML en el mensaje de dedicación?**  Depende de la configuración del editor de texto en Moodle. Si el editor de texto permite HTML, podrás utilizarlo en el mensaje.  Ten en cuenta que el uso excesivo de HTML puede afectar la apariencia y accesibilidad del bloque.  Se recomienda utilizar el formateo proporcionado por el editor de texto.
*   **¿Cómo puedo cambiar la apariencia del bloque?** La apariencia del bloque está controlada por el tema de Moodle que estés utilizando.  Para personalizar la apariencia del bloque, deberás modificar el tema o crear un tema hijo y editar los estilos CSS correspondientes.
*   **¿Puedo agregar imágenes al mensaje de dedicación?**  Depende de la configuración del editor de texto en Moodle. Si el editor de texto permite insertar imágenes, podrás hacerlo.  Asegúrate de que las imágenes sean apropiadas para el tamaño del bloque y que estén optimizadas para la web.
*   **¿Por qué no veo el bloque después de instalarlo?** Asegúrate de haber añadido el bloque a un curso específico y de que la visibilidad del bloque esté configurada correctamente. También verifica que el tema que estás utilizando tenga una región de bloques disponible.
*   **¿Puedo usar este bloque para mostrar información diferente a una dedicación?** Si bien el bloque está diseñado para mostrar mensajes de dedicación, puedes usarlo para mostrar cualquier texto corto y personalizado que desees mostrar en el curso.  Ten en cuenta que el título del bloque indicará el propósito original del bloque.

## 5. Problemas comunes y soluciones

*   **El bloque no se muestra después de la instalación:**
    *   **Solución:** Verifica que el bloque esté activado en la configuración del curso.  Asegúrate de haberlo añadido a una región visible del tema.  Comprueba que el usuario tenga permisos para ver bloques.
*   **El mensaje de dedicación no se muestra correctamente:**
    *   **Solución:** Revisa el código HTML del mensaje (si lo estás usando) para detectar errores de sintaxis.  Verifica que el editor de texto esté configurado correctamente.  Comprueba la configuración del tema para asegurarte de que el bloque esté mostrando el contenido correctamente.
*   **Errores durante la instalación:**
    *   **Solución:** Revisa los requisitos del plugin (versión de Moodle, dependencias).  Asegúrate de que el servidor tenga suficientes recursos para instalar el plugin.  Verifica que el archivo `.zip` del plugin no esté corrupto.

## 6. Enlaces útiles

*   **Repositorio de plugins de Moodle:** https://moodle.org/plugins/block_dedication
*   **GitHub del plugin:** https://github.com/catalyst/moodle-block_dedication
*   **Documentación oficial de Moodle sobre bloques:** https://docs.moodle.org/405/en/Blocks
```