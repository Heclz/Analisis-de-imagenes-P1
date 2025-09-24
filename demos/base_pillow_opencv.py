# demos/base_pillow_opencv.py
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import argparse, os

def cargar_imagen(ruta):
    imagen = Image.open(ruta).convert("RGB")
    plt.imshow(imagen)
    plt.title("Imagen original")
    plt.axis("off")
    plt.show()
    return imagen

def separar_rgb(imagen):
    r, g, b = imagen.split()
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1); plt.imshow(r, cmap='Reds');   plt.title("Componente R"); plt.axis("off")
    plt.subplot(1, 3, 2); plt.imshow(g, cmap='Greens'); plt.title("Componente G"); plt.axis("off")
    plt.subplot(1, 3, 3); plt.imshow(b, cmap='Blues');  plt.title("Componente B"); plt.axis("off")
    plt.tight_layout(); plt.show()

def convertir_a_grises(imagen):
    img_gray = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2GRAY)
    plt.imshow(img_gray, cmap='gray'); plt.title("Imagen en escala de grises"); plt.axis("off"); plt.show()
    return img_gray

def binarizar_imagen(imagen_gris, umbral=128):
    _, binaria = cv2.threshold(imagen_gris, umbral, 255, cv2.THRESH_BINARY)
    plt.imshow(binaria, cmap='gray'); plt.title(f"Binarizada (umbral fijo = {umbral})"); plt.axis("off"); plt.show()
    return binaria

def binarizar_otsu(imagen_gris):
    # Umbral automático de Otsu
    _, bin_otsu = cv2.threshold(imagen_gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.imshow(bin_otsu, cmap='gray'); plt.title("Binarizada (Otsu)"); plt.axis("off"); plt.show()
    return bin_otsu

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", "-i", required=True, help="Ruta a la imagen")
    ap.add_argument("--umbral", type=int, default=128, help="Umbral fijo para binarización")
    ap.add_argument("--out", "-o", default="out", help="Carpeta de salida")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)

    imagen = cargar_imagen(args.image)
    separar_rgb(imagen)
    gris = convertir_a_grises(imagen)

    bin_fijo = binarizar_imagen(gris, umbral=args.umbral)
    bin_otsu = binarizar_otsu(gris)

    # Guarda resultados por si los necesitas en el informe
    Image.fromarray(gris).save(os.path.join(args.out, "gris.png"))
    Image.fromarray(bin_fijo).save(os.path.join(args.out, "binarizada_fijo.png"))
    Image.fromarray(bin_otsu).save(os.path.join(args.out, "binarizada_otsu.png"))

if __name__ == "__main__":
    main()
