import argparse
import os
import cv2

def ecualizacion_grises(gray):
    return cv2.equalizeHist(gray)

def ecualizacion_color_hsv(bgr):
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_eq = cv2.equalizeHist(v)
    hsv_eq = cv2.merge([h, s, v_eq])
    bgr_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
    return bgr_eq

def main():
    parser = argparse.ArgumentParser(description="Demostración de ecualización (grises y HSV-color)")
    parser.add_argument("--image", "-i", required=True, help="Ruta a la imagen")
    parser.add_argument("--out", "-o", default="out", help="Directorio de salida")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    bgr = cv2.imread(args.image)
    if bgr is None:
        raise FileNotFoundError(f"No se pudo leer la imagen: {args.image}")

    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    eq_gray = ecualizacion_grises(gray)
    eq_bgr = ecualizacion_color_hsv(bgr)

    cv2.imwrite(os.path.join(args.out, "demo_eq_gray.png"), eq_gray)
    cv2.imwrite(os.path.join(args.out, "demo_eq_color_hsv.png"), eq_bgr)
    print("Guardado: demo_eq_gray.png, demo_eq_color_hsv.png en", args.out)

if __name__ == "__main__":
    main()
