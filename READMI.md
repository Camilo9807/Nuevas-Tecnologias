Introducción

"App Web Coches Eléctricos" es una aplicación web interactiva diseñada para analizar y visualizar datos de coches eléctricos registrados. Utiliza un archivo CSV (registros_carros_electricos.csv) como fuente de datos, permitiendo a los usuarios filtrar información y explorar estadísticas a través de tablas y gráficos.

Funcionalidades Principales

Esta aplicación ofrece las siguientes características clave:





Filtrado de Datos: Permite filtrar por:





Marca del coche



Año de registro



Autonomía (en kilómetros)



Tipo de carga (rápida, normal, etc.)



Fecha de registro



Baterías recicladas (sí/no)



Edad del dueño



Visualización de Datos:





Tabla dinámica con los datos filtrados.



Gráficos interactivos que incluyen:





Cantidad de autos por marca



Distribución de autonomía



Tipos de carga más comunes



Autonomía promedio por año



Proporción de baterías recicladas

Requisitos





Python 3.x instalado



Bibliotecas necesarias: streamlit, pandas, plotly



Archivo CSV: registros_carros_electricos.csv

Cómo Usarlo

Sigue estos pasos para configurar y usar la aplicación:





Instalación de Dependencias
Abre una terminal y ejecuta:

pip install streamlit pandas plotly



Preparar el Archivo de Datos
Asegúrate de que el archivo registros_carros_electricos.csv esté en la misma carpeta que el script de la aplicación.



Ejecutar la Aplicación
En la terminal, navega a la carpeta del script y escribe:

streamlit run app.py

Esto abrirá la aplicación en tu navegador predeterminado.



Interactuar con la Aplicación





Usa la barra lateral para seleccionar filtros (por ejemplo, marca o año).



Explora la tabla con los datos filtrados.



Revisa los gráficos generados automáticamente según tus selecciones.

Ejemplos de Uso

Aquí hay algunos ejemplos prácticos para que veas cómo funciona:





Filtrar Coches Tesla de 2023
En la barra lateral, selecciona "Tesla" en el filtro de marca y "2023" en el filtro de año. La tabla mostrará solo los Tesla registrados en 2023, y los gráficos se actualizarán para reflejar esta selección.



Analizar Tipos de Carga
Activa el filtro de "baterías recicladas" y selecciona "Sí". Luego, revisa el gráfico de tipos de carga para ver qué métodos predominan entre los coches con baterías recicladas.

Beneficios





Fácil de Usar: Interfaz intuitiva con filtros simples y visualizaciones claras.



Visual: Gráficos interactivos que facilitan el análisis de datos.



Directo: Obtén información útil sin complicaciones.

Notas Adicionales





Asegúrate de que el archivo CSV tenga las columnas esperadas (marca, año, autonomía, etc.) para que la aplicación funcione correctamente.



Si necesitas personalizar los gráficos o filtros, puedes modificar el código en app.py.