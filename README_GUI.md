# GUI unificada – Práctica 1

Este proyecto ahora incluye una interfaz sencilla (`gui_menu.py`) para lanzar **todos los demos** de la carpeta `demos/` y el **análisis principal** (`analyze_image.py`) sobre una imagen que selecciones.

## Requisitos
1. Crear y activar un entorno virtual (opcional pero recomendado).
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Uso
Desde la carpeta del proyecto:

```bash
python gui_menu.py
```

1. **Selecciona una imagen** (puedes elegir cualquier ruta; no es obligatorio copiarla a `imgs/`).
2. Marca/desmarca las tareas que quieras ejecutar:
   - Lectura/RGB/Grises/Binarización (usa `demos/base_pillow_opencv.py`)
   - Histogramas + CDF + Binarización (grises) (usa `demos/hist_gray_binarize.py`)
   - HSV + Ecualización (canal V) (usa `demos/hsv_model_demo.py`)
   - Ecualización (Grises y Color) (usa `demos/ecualizacion_demo.py`)
   - Análisis Principal (grises+color+métricas) (usa `analyze_image.py --all`)
3. Ajusta el **umbral** si lo deseas (para las tareas que lo usan).
4. Presiona **“Ejecutar seleccionados”**. Los resultados se guardarán en `out/` y el log se muestra en pantalla.
5. Con **“Abrir carpeta out/”** puedes abrir el directorio de resultados.

> La interfaz llama a los scripts existentes mediante el mismo intérprete de Python que la ejecuta (`sys.executable`).

## Notas
- Si alguna tarea no encuentra su script, se omitirá y se informará en el log.
- Verifica que `opencv-python`, `numpy`, `matplotlib` y `Pillow` estén instalados.
- Si tu sistema no abre la carpeta `out/` desde el botón, ábrela manualmente desde tu explorador de archivos.

—
Archivo generado automáticamente por ChatGPT.
