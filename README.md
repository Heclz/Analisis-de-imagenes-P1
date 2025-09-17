PRACTICA 1 — Análisis de Imágenes con Python (Equipo Supernovas)

Objetivo. Aplicar conceptos fundamentales del análisis de imágenes digitales mediante el desarrollo colaborativo de scripts en Python para leer, transformar y analizar imágenes, relacionando los modelos de color con el procesamiento básico. 

Practica 1-Analisis de Imágenes

Alcance y productos por sesión

Sesión 1 (90 min): lectura de imágenes, separación RGB, breve repaso de modelos de color; producto: script que lee y separa RGB + bitácora. 

Practica 1-Analisis de Imágenes

 

Practica 1-Analisis de Imágenes

Sesión 2 (90 min): grises, binarización (umbral fijo y Otsu) y histograma de intensidad; producto: script que escale a grises y binarice + comparación de resultados. 

Practica 1-Analisis de Imágenes

 

Practica 1-Analisis de Imágenes

Sesión 3 (90 min): presentación y reflexión; productos: informe técnico y repositorio en GitHub con código y documentación. 

Practica 1-Analisis de Imágenes

Rúbrica (criterios de evaluación)

Funcionalidad del código, aplicación de modelos de color, transformaciones (grises/binarización), trabajo colaborativo, presentación y documentación, y reflexión/mejora autónoma. Usa esta lista como checklist al cerrar issues/PRs. 

Practica 1-Analisis de Imágenes

 

Practica 1-Analisis de Imágenes

 

Practica 1-Analisis de Imágenes

Requisitos

Python 3.x instalado. 

Guia_Laboratorio_Analisis_Image…

Librerías: pillow, opencv-python, numpy, matplotlib. 

Guia_Laboratorio_Analisis_Image…

Se recomienda entorno virtual para evitar conflictos de versiones. 

Practica 1-Analisis de Imágenes

Instalación rápida

Windows (PowerShell)

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt


macOS / Linux

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Si no usas requirements.txt, instala directo:

pip install pillow opencv-python numpy matplotlib


Guia_Laboratorio_Analisis_Image…

Estructura sugerida del repositorio
.
├─ src/
│  └─ analisis_imagenes.py        # script principal (RGB, grises, binarización)
├─ data/
│  └─ imagen_ejemplo.jpg          # imagen de prueba (colócala aquí)
├─ docs/
│  ├─ informe_tecnico.docx        # entrega final
│  └─ presentacion.pptx           # diapositivas
├─ reports/figuras/               # capturas (RGB/gris/binaria/histograma)
├─ notebooks/                     # (opcional)
├─ README.md
└─ requirements.txt

Uso

Coloca una imagen de prueba en data/ y ajusta ruta_imagen en el script.

Ejecuta el script y observa cada transformación (RGB → grises → binarización).

Prueba distintos umbrales y agrega funciones (p. ej., HSV con OpenCV). 

Practica 1-Analisis de Imágenes

 

Practica 1-Analisis de Imágenes

Ejecutar

python src/analisis_imagenes.py


Código base (punto de partida de la práctica: lectura, separación RGB, grises, binarización) está descrito en el anexo de la práctica. 

Practica 1-Analisis de Imágenes

Roadmap por sesiones (issues sugeridos)

S1

feat: lectura de imagen y separación RGB

docs: bitácora sesión 1

S2

feat: conversión a grises

feat: binarización (umbral fijo) + (Otsu)

feat: histograma de intensidad

exp: comparación RGB vs HSV

S3

docs: informe técnico (IMRyD) + anexos

chore: preparar demo y presentación

release: publicar repo final

Estas tareas están alineadas con los productos esperados de cada sesión. 

Practica 1-Analisis de Imágenes

 

Practica 1-Analisis de Imágenes

Guía de colaboración (Git)

Flujo propuesto: ramas main (protegida), dev, feature/<tarea>.

Pull Requests con:

Descripción breve del cambio.

Evidencias (capturas de RGB, grises, binaria, histograma en reports/figuras/).

Checklist de rúbrica (ver arriba).

Bitácoras de cada sesión y reparto de roles documentados (Notion/docs/), como solicita la guía. 

Guia_Laboratorio_Analisis_Image…

Roles del equipo (Supernovas)

Cruz Mejía Alexa Belem — Secretaría / Documentación

García Martínez Jair Salvador — Coordinación / Crítica / Investigación

Lopez Martínez Hector Alexis — Portavoz / Programación

Maza Orozco Josue Vicente — Control de calidad / Investigación

(Ajusta @menciones en GitHub Projects / Notion según corresponda).
