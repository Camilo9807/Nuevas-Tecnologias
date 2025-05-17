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

Notas Adicionales
- Asegúrate de mantener el archivo `requirements.txt` actualizado con las dependencias necesarias para el proyecto.
- Recuerda desactivar el entorno virtual cuando termines de trabajar ejecutando `deactivate`.

¡Con estos pasos, el proyecto está listo para ser desarrollado!
```