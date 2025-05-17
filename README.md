🚀 Proyecto en Python — Guía de Configuración

Bienvenido al repositorio de este proyecto en Python. A continuación encontrarás una guía clara y paso a paso para configurar el entorno de desarrollo, instalar dependencias y dejar todo listo para comenzar a programar.

---

🧰 Pasos de Configuración

✅ 1. Crear el Entorno Virtual
Para mantener un entorno limpio y libre de conflictos, se utilizó el módulo `venv` de Python:

```bash
python3 -m venv venv

```

2. Activación del Entorno Virtual
Una vez creado el entorno virtual, se activó para que las dependencias se instalen en el entorno aislado.

- En sistemas Unix/MacOS:
    ```bash
    source venv/bin/activate
    ```
- En sistemas Windows:
    ```bash
    .\venv\Scripts\activate
    ```

3. Instalación de Dependencias
Con el entorno virtual activado, se instalaron las dependencias necesarias para el proyecto utilizando `pip`.

```bash
pip install -r requirements.txt
```

4. Confirmación de la Configuración
Para verificar que todo estaba correctamente configurado, se comprobó la lista de paquetes instalados y la versión de Python activa.

```bash
pip list
python --version
```

.

🔍 Explorando la Aplicación: Filtrado y Visualización de Datos
Este proyecto ofrece una interfaz interactiva construida con Streamlit para analizar registros de coches eléctricos. A continuación, se describen las funcionalidades principales:

⚙️ Barra Lateral de Filtros
En la barra lateral, encontrarás una serie de filtros interactivos que te permitirán segmentar los datos según tus intereses:

Marca del Auto: Selecciona una o varias marcas de coches eléctricos para enfocar tu análisis.
Año del Modelo: Utiliza un slider para definir el rango de años de los modelos que deseas visualizar.
Autonomía (km): Filtra los coches por su rango de autonomía en kilómetros.
Tipo de Carga: Elige uno o varios tipos de carga para analizar los registros correspondientes.
Fecha de Registro: Selecciona un rango de fechas para analizar los registros dentro de ese período.
Baterías Recicladas: Filtra los coches según si sus baterías son recicladas (Sí/No/Todos).
Edad del Propietario: Utiliza un slider para analizar los registros por el rango de edad de los propietarios.
📊 Visualizaciones Interactivas
Una vez que hayas aplicado los filtros, la aplicación mostrará un DataFrame con los datos filtrados y varias visualizaciones interactivas para ayudarte a comprender las tendencias:

Autos por Marca (Expandible): Un gráfico de barras que muestra el número de coches por cada marca seleccionada.
Distribución de Autonomía (Expandible): Un histograma que muestra la distribución de la autonomía en kilómetros de los coches filtrados.
Distribución de Tipos de Carga (Expandible): Un gráfico de pastel que muestra la proporción de cada tipo de carga entre los coches filtrados.
Autonomía vs. Año del Modelo (Expandible): Un gráfico de dispersión que relaciona la autonomía de los coches con su año de modelo, permitiendo identificar tendencias a lo largo del tiempo. Al pasar el cursor, se muestra la marca y el modelo del auto.
Baterías Recicladas (Expandible): Un gráfico de barras que compara la cantidad de coches con baterías recicladas y no recicladas.
⚠️ Advertencia
Si no hay datos que coincidan con los filtros seleccionados, se mostrará una advertencia indicando que no hay información disponible.



Notas Adicionales
- Asegúrate de mantener el archivo `requirements.txt` actualizado con las dependencias necesarias para el proyecto.
- Recuerda desactivar el entorno virtual cuando termines de trabajar ejecutando `deactivate`.

¡Con estos pasos, el proyecto está listo para ser desarrollado!
```