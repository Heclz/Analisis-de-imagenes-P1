#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI unificada para ejecutar los demos y el análisis principal
del proyecto "Práctica 1: Histograma y Propiedades".

Requisitos: Python 3.9+, dependencias de requirements.txt.
Uso:
    python gui_menu.py
"""

import os
import sys
import threading
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# -------- Utilidades de ruta --------
SCRIPT_DIR = Path(__file__).resolve().parent
DEMOS_DIR = SCRIPT_DIR / "demos"
OUT_DIR   = SCRIPT_DIR / "out"

PYTHON = sys.executable  # Interpretador actual de Python

# --------- Ejecuciones disponibles ---------
# Mapeamos "tareas" a comandos. Algunos usan --umbral.
TASKS = {
    "Lectura/RGB/Grises/Binarización": {
        "script": DEMOS_DIR / "base_pillow_opencv.py",
        "args": ["--image", None, "--umbral", None],  # completaremos en tiempo de ejecución
        "needs_threshold": True
    },
    "Histogramas + CDF + Binarización (grises)": {
        "script": DEMOS_DIR / "hist_gray_binarize.py",
        "args": ["--image", None, "--umbral", None],
        "needs_threshold": True
    },
    "HSV + Ecualización (canal V)": {
        "script": DEMOS_DIR / "hsv_model_demo.py",
        "args": ["--image", None],
        "needs_threshold": False
    },
    "Ecualización (Grises y Color)": {
        "script": DEMOS_DIR / "ecualizacion_demo.py",
        "args": ["--image", None],
        "needs_threshold": False
    },
    "Análisis Principal (grises+color+métricas)": {
        "script": SCRIPT_DIR / "analyze_image.py",
        "args": ["--image", None, "--all"],
        "needs_threshold": False
    },
}

def ensure_out_dir():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

def open_out_folder():
    ensure_out_dir()
    try:
        if sys.platform.startswith("win"):
            os.startfile(str(OUT_DIR))
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(OUT_DIR)])
        else:
            subprocess.Popen(["xdg-open", str(OUT_DIR)])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir la carpeta 'out': {e}")

# --------- Worker de ejecución en hilo ---------
class Runner(threading.Thread):
    def __init__(self, image_path, selections, threshold, log_fn):
        super().__init__(daemon=True)
        self.image_path = image_path
        self.selections = selections  # lista de nombres (keys de TASKS) seleccionados
        self.threshold = threshold
        self.log = log_fn

    def run(self):
        ensure_out_dir()
        for task_name in self.selections:
            spec = TASKS.get(task_name)
            if spec is None:
                self.log(f"[WARN] Tarea desconocida: {task_name}\n")
                continue

            script_path = spec["script"]
            if not script_path.exists():
                self.log(f"[SKIP] No se encontró el script: {script_path}\n")
                continue

            # Construir comando
            cmd = [PYTHON, str(script_path)]
            args = list(spec["args"])
            # Rellenar la ruta de imagen
            for i, a in enumerate(args):
                if a is None:
                    # colocar la image_path (para primer None) o threshold si se requiere
                    if "--image" in args[i-1]:
                        args[i] = self.image_path
                    elif "--umbral" in args[i-1]:
                        args[i] = str(self.threshold)
            cmd.extend(args)

            self.log(f"$ {' '.join(cmd)}\n")
            try:
                # Ejecutar subproceso
                proc = subprocess.Popen(cmd, cwd=str(SCRIPT_DIR), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                for line in proc.stdout:
                    self.log(line)
                ret = proc.wait()
                if ret == 0:
                    self.log(f"[OK] {task_name} finalizado.\n\n")
                else:
                    self.log(f"[ERROR] {task_name} terminó con código {ret}.\n\n")
            except Exception as e:
                self.log(f"[EXCEPTION] {task_name}: {e}\n\n")

# --------- Interfaz ---------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú unificado – Práctica 1 (Histogramas y Propiedades)")
        self.geometry("820x600")
        self.minsize(740, 520)

        # Estado
        self.image_path_var = tk.StringVar(value="")
        self.threshold_var = tk.IntVar(value=128)
        self.task_vars = {name: tk.BooleanVar(value=True) for name in TASKS.keys()}

        # Layout
        self._build_ui()

    def _build_ui(self):
        # Frame superior: selección de imagen
        top = ttk.LabelFrame(self, text="1) Selecciona una imagen")
        top.pack(fill="x", padx=12, pady=8)

        row = ttk.Frame(top)
        row.pack(fill="x", padx=8, pady=8)

        ttk.Label(row, text="Ruta de imagen:").pack(side="left")
        entry = ttk.Entry(row, textvariable=self.image_path_var)
        entry.pack(side="left", fill="x", expand=True, padx=8)
        ttk.Button(row, text="Buscar...", command=self.choose_image).pack(side="left")

        # Frame medio: opciones
        middle = ttk.LabelFrame(self, text="2) Elige qué ejecutar")
        middle.pack(fill="both", expand=True, padx=12, pady=8)

        # Checkboxes en grid
        grid = ttk.Frame(middle)
        grid.pack(fill="x", padx=8, pady=8)

        for i, name in enumerate(TASKS.keys()):
            ttk.Checkbutton(grid, text=name, variable=self.task_vars[name]).grid(row=i, column=0, sticky="w", pady=2)

        thr = ttk.Frame(middle)
        thr.pack(fill="x", padx=8, pady=(6,2))
        ttk.Label(thr, text="Umbral (para binarización):").pack(side="left")
        ttk.Spinbox(thr, from_=0, to=255, textvariable=self.threshold_var, width=6).pack(side="left", padx=6)

        # Frame acciones
        actions = ttk.Frame(self)
        actions.pack(fill="x", padx=12, pady=(0,6))

        ttk.Button(actions, text="Ejecutar seleccionados", command=self.run_selected).pack(side="left")
        ttk.Button(actions, text="Abrir carpeta out/", command=open_out_folder).pack(side="left", padx=8)

        # Log
        logframe = ttk.LabelFrame(self, text="Salida / Log")
        logframe.pack(fill="both", expand=True, padx=12, pady=(4,10))
        self.logtext = tk.Text(logframe, height=12, wrap="word")
        self.logtext.pack(fill="both", expand=True)
        self.logtext.insert("end", "Listo. Selecciona una imagen y ejecuta las tareas.\n")

    def choose_image(self):
        ftypes = [
            ("Imágenes", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"),
            ("Todos los archivos", "*.*")
        ]
        path = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=ftypes, initialdir=str(SCRIPT_DIR / "imgs"))
        if path:
            self.image_path_var.set(path)

    def run_selected(self):
        img = self.image_path_var.get().strip()
        if not img:
            messagebox.showwarning("Falta imagen", "Selecciona una imagen primero.")
            return
        if not os.path.exists(img):
            messagebox.showerror("Ruta inválida", "La ruta de la imagen no existe.")
            return

        selections = [name for name, var in self.task_vars.items() if var.get()]
        if not selections:
            messagebox.showwarning("Nada seleccionado", "Marca al menos una tarea para ejecutar.")
            return

        threshold = int(self.threshold_var.get())

        self.append_log(f"\n== Ejecutando {len(selections)} tarea(s) sobre: {img}\n")
        runner = Runner(img, selections, threshold, self.append_log)
        runner.start()

    def append_log(self, text: str):
        self.logtext.insert("end", text)
        self.logtext.see("end")
        self.update_idletasks()

if __name__ == "__main__":
    App().mainloop()
