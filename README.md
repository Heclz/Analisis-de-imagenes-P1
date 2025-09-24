# Extensión – Práctica 1: Histograma y Propiedades (Color y Escala de Grises)

Este proyecto calcula **histogramas** y **propiedades estadísticas** (energía, entropía, asimetría, media, varianza) para:
- **Imagen en escala de grises**
- **Imagen en color (RGB)** — por canal (Rojo, Verde, Azul)

Además incluye **extensiones** útiles para el desarrollo posterior:
- Histograma **acumulado (CDF)** y **normalizado**
- **Kurtosis** (opcional, para mayor análisis)
- **Ecualización** de histograma (grises y aproximación en color)
- Exportación a **CSV/JSON** de resultados
- Guardado de gráficas (PNG) y resultados

> Coloca tus imágenes dentro de `imgs/` y usa rutas como `imgs/mi_imagen.jpg`.

---

## 1) Requisitos

Python 3.9+ recomendado. Instala dependencias con:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 2) Cómo ejecutar

### A) Análisis principal (grises + color)
```bash
python analyze_image.py --image imgs/tu_imagen.jpg --all
```
**Genera en `out/`:**
- **Grises**
  - `hist_gray.png` (histograma), `hist_gray_cdf.png` (CDF)
  - `hist_eq_gray.png` (imagen ecualizada)
  - `stats_gray.json`, `stats_gray.csv` (energía, entropía, asimetría, media, varianza, kurtosis)
- **Color (por canal R, G, B)**
  - `hist_R.png`, `hist_G.png`, `hist_B.png` (histogramas por canal)
  - `cdf_R.png`, `cdf_G.png`, `cdf_B.png` (CDF por canal)
  - `color_eq_hsv.png` (ecualización aproximada en HSV, canal V)
  - `stats_color.json`, `stats_color.csv` (métricas por canal)

### B) Solo **escala de grises**
```bash
python analyze_image.py --image imgs/tu_imagen.jpg --gray
```

### C) Solo **color (RGB por canal)**
```bash
python analyze_image.py --image imgs/tu_imagen.jpg --color
```

### D) Ver en pantalla (además de guardar)
Añade `--show` para abrir **figuras** (histogramas/CDF).
> Si quieres ventanas con **imágenes** (original/ecualizada), usa los demos de abajo.

---

## 3) Demos (comandos y salidas)

> Todos guardan resultados en `out/` y muestran ventanas (si tu entorno tiene GUI).

### 3.1 Lectura, separación **RGB**, **grises** y **binarización** (fijo + Otsu)
```bash
python demos/base_pillow_opencv.py --image imgs/tu_imagen.jpg --umbral 128
```
**Genera:**  
`gris.png`, `binarizada_fijo.png`, `binarizada_otsu.png`

### 3.2 **Histogramas + CDF** en grises y **binarización**
```bash
python demos/hist_gray_binarize.py --image imgs/tu_imagen.jpg
# opcional: --umbral 100
```
**Genera:**  
`hist_gray.png`, `hist_gray_cdf.png`, `bin_fixed.png`, `bin_otsu.png`

### 3.3 Modelo de color **HSV** (H/S/V) + ecualización de **V**
```bash
python demos/hsv_model_demo.py --image imgs/tu_imagen.jpg
```
**Genera:**  
`hsv_v_equalized.png`

### 3.4 Demo de **ecualización** (grises y color)
```bash
python demos/ecualizacion_demo.py --image imgs/tu_imagen.jpg
```
**Genera:**  
`demo_eq_gray.png`, `demo_eq_color_hsv.png`

---

## 4) Estructura del proyecto

```
practica1_histograma_proyecto/
├── analyze_image.py           # CLI principal (color/grises, métricas, gráficas)
├── metrics.py                 # Cálculo de métricas y utilidades
├── demos/
│   ├── base_pillow_opencv.py  # Lectura, RGB, grises, binarización (fijo/Otsu)
│   ├── hist_gray_binarize.py  # Histograma + CDF + binarizaciones (grises)
│   ├── hsv_model_demo.py      # Canales H/S/V y ecualización en V
│   └── ecualizacion_demo.py   # Ecualización en grises y color (HSV)
├── imgs/                      # Coloca aquí tus imágenes
│   └── ejemplo.jpg            # (placeholder)
├── out/                       # Resultados: png/csv/json
├── requirements.txt
└── README.md
```

---

## 5) Relación con la práctica solicitada

- **Histograma** y **propiedades estadísticas** para **color** (R,G,B) y **grises**: implementado en `metrics.py` y orquestado por `analyze_image.py`.
- Propiedades: **energía**, **entropía**, **asimetría (skewness)**, **media**, **varianza** (y **kurtosis** opcional).
- Extensiones: **CDF**, **ecualización**, **exportación** a **CSV/JSON**.

---

## 6) Notas y tips

- Formatos recomendados: **JPG/PNG/BMP/TIFF 8-bit por canal** (0–255). Evita CMYK.
- Si tu imagen es **16-bit/HDR**, conviértela a 8-bit para que los histogramas (256 bins) tengan sentido.
- En Windows, abre rápido:  
  ```powershell
  start .\out\hist_eq_gray.png
  start .\out\color_eq_hsv.png
  ```
- La ecualización en color se hace en **HSV** (canal **V**) como aproximación; puedes probar **YCrCb** (canal **Y**) si lo requiere tu análisis.

---

### Roles del equipo (Supernovas)

- **Cruz Mejía Alexa Belem** — Secretaría / Documentación
- **García Martínez Jair Salvador** — Coordinación / Crítica / Investigación
- **Lopez Martínez Hector Alexis** — Portavoz / Programación
- **Maza Orozco Josue Vicente** — Control de calidad / Investigación

*(Ajusta @menciones en GitHub Projects / Notion según corresponda).*
