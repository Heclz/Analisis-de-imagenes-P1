# demos/hsv_model_demo.py
import argparse, os, cv2, matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", "-i", required=True)
    ap.add_argument("--out", "-o", default="out")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    bgr = cv2.imread(args.image)
    if bgr is None:
        raise FileNotFoundError(f"No se pudo leer: {args.image}")

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    # Mostrar canales H, S, V
    plt.figure(figsize=(12,4))
    plt.subplot(1,3,1); plt.imshow(h, cmap="hsv");   plt.title("H (Tono)");     plt.axis("off")
    plt.subplot(1,3,2); plt.imshow(s, cmap="gray");  plt.title("S (Saturación)");plt.axis("off")
    plt.subplot(1,3,3); plt.imshow(v, cmap="gray");  plt.title("V (Valor)");     plt.axis("off")
    plt.tight_layout(); plt.show()

    # Ejemplo de ecualizar V (mejora contraste) y reconstruir
    v_eq = cv2.equalizeHist(v)
    hsv_eq = cv2.merge([h, s, v_eq])
    bgr_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
    cv2.imwrite(os.path.join(args.out, "hsv_v_equalized.png"), bgr_eq)

if __name__ == "__main__":
    main()
