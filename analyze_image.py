import argparse
import os
import json
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

from metrics import compute_stats_from_data, histogram_and_prob, cumulative_hist

# --------- Auxiliares de graficación ---------

def save_hist_plot(hist, title, out_path, color=None, show=False):
    plt.figure()
    plt.title(title)
    plt.xlabel("Intensidad")
    plt.ylabel("Frecuencia")
    if color is not None:
        # No imponemos estilos; 'color' es opcional (p.ej., 'r','g','b','gray')
        plt.plot(hist, color=color)
    else:
        plt.plot(hist)
    plt.grid(True)
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()

def save_cdf_plot(cdf, title, out_path, color=None, show=False):
    plt.figure()
    plt.title(title)
    plt.xlabel("Intensidad")
    plt.ylabel("Probabilidad acumulada")
    if color is not None:
        plt.plot(cdf, color=color)
    else:
        plt.plot(cdf)
    plt.grid(True)
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    if show:
        plt.show()
    plt.close()

def export_dict_json_csv(d, json_path, csv_path):
    # JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    # CSV
    # Convertimos dict -> filas
    rows = []
    for k, v in d.items():
        if isinstance(v, dict):
            row = {"nombre": k}
            row.update(v)
            rows.append(row)
        else:
            rows.append({"nombre": k, "valor": v})
    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False, encoding="utf-8")

# --------- Procesos ---------

def analyze_gray(img, out_dir, show=False):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    data = gray.flatten()
    hist, prob, stats = compute_stats_from_data(data, include_kurtosis=True)
    cdf = cumulative_hist(prob)

    # Guardar gráficas
    save_hist_plot(hist, "Histograma (Grises)", os.path.join(out_dir, "hist_gray.png"), color="gray", show=show)
    save_cdf_plot(cdf, "CDF (Grises)", os.path.join(out_dir, "hist_gray_cdf.png"), color="gray", show=show)

    # Ecualización de grises (extensión)
    eq = cv2.equalizeHist(gray)
    cv2.imwrite(os.path.join(out_dir, "hist_eq_gray.png"), eq)

    # Resultados
    results = {"grises": stats}
    export_dict_json_csv(results,
                         os.path.join(out_dir, "stats_gray.json"),
                         os.path.join(out_dir, "stats_gray.csv"))
    return results

def analyze_color(img, out_dir, show=False):
    # Convertimos BGR -> RGB solo para consistencia de canales al graficar
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    channel_names = ["Rojo", "Verde", "Azul"]
    channel_colors = ["r", "g", "b"]
    results = {}

    for i, name in enumerate(channel_names):
        data = rgb[:, :, i].flatten()
        hist, prob, stats = compute_stats_from_data(data, include_kurtosis=True)
        cdf = cumulative_hist(prob)

        # Gráficas por canal
        save_hist_plot(hist, f"Histograma {name}", os.path.join(out_dir, f"hist_{name[0]}.png"), color=channel_colors[i], show=show)
        save_cdf_plot(cdf, f"CDF {name}", os.path.join(out_dir, f"cdf_{name[0]}.png"), color=channel_colors[i], show=show)

        results[name] = stats

    # Ecualización aproximada en color (HSV: ecualizamos V)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v_eq = cv2.equalizeHist(v)
    hsv_eq = cv2.merge([h, s, v_eq])
    bgr_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
    cv2.imwrite(os.path.join(out_dir, "color_eq_hsv.png"), bgr_eq)

    export_dict_json_csv(results,
                         os.path.join(out_dir, "stats_color.json"),
                         os.path.join(out_dir, "stats_color.csv"))
    return results

# --------- CLI ---------

def main():
    parser = argparse.ArgumentParser(description="Práctica 1: Histogramas y Propiedades (grises y color)")
    parser.add_argument("--image", "-i", required=True, help="Ruta a la imagen de entrada (jpg/png, etc.)")
    parser.add_argument("--out", "-o", default="out", help="Carpeta de salida (por defecto: out)")
    parser.add_argument("--gray", action="store_true", help="Analizar solo escala de grises")
    parser.add_argument("--color", action="store_true", help="Analizar solo color (RGB)")
    parser.add_argument("--all", action="store_true", help="Analizar ambos (grises y color)")
    parser.add_argument("--show", action="store_true", help="Mostrar figuras además de guardarlas")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    img = cv2.imread(args.image)
    if img is None:
        raise FileNotFoundError(f"No se pudo leer la imagen: {args.image}. ¿Ruta correcta?")

    if args.all or (not args.gray and not args.color):
        # Por defecto, si no especifica, hacemos ambos
        gray_res = analyze_gray(img, args.out, show=args.show)
        color_res = analyze_color(img, args.out, show=args.show)
        print("== Resumen (Grises) ==")
        print(json.dumps(gray_res, indent=2, ensure_ascii=False))
        print("== Resumen (Color por canal) ==")
        print(json.dumps(color_res, indent=2, ensure_ascii=False))
    else:
        if args.gray:
            gray_res = analyze_gray(img, args.out, show=args.show)
            print("== Resumen (Grises) ==")
            print(json.dumps(gray_res, indent=2, ensure_ascii=False))

        if args.color:
            color_res = analyze_color(img, args.out, show=args.show)
            print("== Resumen (Color por canal) ==")
            print(json.dumps(color_res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
