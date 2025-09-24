# demos/hist_gray_binarize.py
import argparse, os, numpy as np, cv2, matplotlib.pyplot as plt

def mostrar_y_guardar_hist(gray, outdir):
    # Histograma 0..255 (256 bins)
    hist, bins = np.histogram(gray.flatten(), bins=256, range=(0, 256))
    prob = hist / np.sum(hist) if np.sum(hist) > 0 else np.zeros_like(hist, dtype=float)
    cdf = np.cumsum(prob)

    # Histograma
    plt.figure(); plt.title("Histograma (Grises)")
    plt.xlabel("Intensidad"); plt.ylabel("Frecuencia")
    plt.plot(hist); plt.grid(True)
    plt.savefig(os.path.join(outdir, "hist_gray.png"), dpi=150, bbox_inches="tight")
    plt.show()

    # CDF
    plt.figure(); plt.title("CDF (Grises)")
    plt.xlabel("Intensidad"); plt.ylabel("Probabilidad acumulada")
    plt.plot(cdf); plt.grid(True)
    plt.savefig(os.path.join(outdir, "hist_gray_cdf.png"), dpi=150, bbox_inches="tight")
    plt.show()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", "-i", required=True)
    ap.add_argument("--out", "-o", default="out")
    ap.add_argument("--umbral", type=int, default=128)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    bgr = cv2.imread(args.image)
    if bgr is None:
        raise FileNotFoundError(f"No se pudo leer: {args.image}")

    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    mostrar_y_guardar_hist(gray, args.out)

    # Binarización fija
    _, bin_fijo = cv2.threshold(gray, args.umbral, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(args.out, "bin_fixed.png"), bin_fijo)

    # Otsu automático
    _, bin_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(os.path.join(args.out, "bin_otsu.png"), bin_otsu)

if __name__ == "__main__":
    main()
