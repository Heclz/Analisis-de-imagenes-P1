# Extensión – Práctica 1: Histograma y Propiedades (Color y Escala de Grises)

Este proyecto calcula **histogramas** y **propiedades estadísticas** (energía, entropía, asimetría, media, varianza) para:
- **Imagen en escala de grises**
- **Imagen en color (RGB)** — por canal (Rojo, Verde, Azul)

Además incluye **extensiones** útiles para el desarrollo posterior:
- Histograma **acumulado** y **normalizado**
- **Kurtosis** (opcional, para mayor análisis)
- **Ecualización** de histograma (grises y aproximación en color)
- Exportación a **CSV/JSON** de resultados
- Guardado de gráficas (PNG) y resultados

> Sugerencia: coloca tus imágenes dentro de la carpeta `imgs/` y usa rutas como `imgs/mi_imagen.jpg`.

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

### A) Análisis completo (grises y color) con una sola orden
```bash
python analyze_image.py --image imgs/tu_imagen.jpg --all
```
Genera:
- Carpeta `out/` con:
  - `hist_gray.png`, `hist_gray_cdf.png`, `hist_eq_gray.png` (si aplica)
  - `hist_R.png`, `hist_G.png`, `hist_B.png` y sus CDFs
  - `stats_gray.json`, `stats_color.json` y `stats_*.csv`

### B) Solo **escala de grises**
```bash
python analyze_image.py --image imgs/tu_imagen.jpg --gray
```

### C) Solo **color (RGB por canal)**
```bash
python analyze_image.py --image imgs/tu_imagen.jpg --color
```

### D) Demo de ecualización (grises y color)
```bash
python demos/ecualizacion_demo.py --image imgs/tu_imagen.jpg
```

> Si necesitas ver los resultados en pantalla (además de guardarlos), añade `--show` en los comandos.

---

## 3) Estructura del proyecto

```
practica1_histograma_proyecto/
├── analyze_image.py           # CLI principal (color/grises)
├── metrics.py                 # Cálculo de métricas y utilidades
├── demos/
│   └── ecualizacion_demo.py   # Ejemplos de ecualización (grises/HSV)
├── imgs/                      # Coloca aquí tus imágenes
│   └── ejemplo.jpg            # (placeholder vacío, reemplázalo por tu imagen)
├── out/                       # Resultados: png/csv/json
├── requirements.txt
└── README.md
```

---

## 4) Relación con la práctica solicitada

- **Histograma** y **propiedades estadísticas** para **color** (R,G,B) y **grises**: implementado en `metrics.py` y orquestado por `analyze_image.py`.
- Propiedades: **energía**, **entropía**, **asimetría (skewness)**, **media**, **varianza**.
- Extensiones sugeridas: **CDF**, **ecualización**, **exportación** (CSV/JSON) para apoyar el desarrollo posterior y la autoevaluación.

---

## 5) Notas

- Las gráficas se guardan en `out/`. Si usas `--show`, se abrirán ventanas interactivas (puede no ser deseable en servidores headless).
- Las estadísticas se imprimen y guardan en JSON/CSV.
- La ecualización en color se hace en el espacio **HSV** (ecualizando el canal V) como aproximación; también puedes experimentar con **YCrCb** (ecualizando **Y**).

Roles del equipo (Supernovas)

Cruz Mejía Alexa Belem — Secretaría / Documentación

García Martínez Jair Salvador — Coordinación / Crítica / Investigación

Lopez Martínez Hector Alexis — Portavoz / Programación

Maza Orozco Josue Vicente — Control de calidad / Investigación

(Ajusta @menciones en GitHub Projects / Notion según corresponda).
