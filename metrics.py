import numpy as np
from math import log2
from scipy.stats import skew, kurtosis

def histogram_and_prob(data, bins=256):
    """Devuelve histograma y distribución de probabilidad normalizada."""
    hist, bin_edges = np.histogram(data, bins=bins, range=(0, 256))
    total = hist.sum()
    prob = hist / total if total > 0 else np.zeros_like(hist, dtype=float)
    return hist, prob, bin_edges

def energy(prob):
    """Energía: sumatoria de p_i^2."""
    return float(np.sum(prob ** 2))

def entropy(prob):
    """Entropía de Shannon (base 2), ignorando p_i=0."""
    return float(-np.sum([p * log2(p) for p in prob if p > 0]))

def skewness(data):
    """Asimetría (skewness)."""
    return float(skew(data))

def mean(data):
    return float(np.mean(data))

def variance(data):
    return float(np.var(data))

def kurtosis_excess(data):
    """Kurtosis (exceso). Útil como extensión opcional."""
    return float(kurtosis(data))

def cumulative_hist(prob):
    """Distribución acumulada (CDF) a partir de probabilidad por bins."""
    return np.cumsum(prob)

def compute_stats_from_data(data, include_kurtosis=True):
    """Calcula estadísticas estándar (y kurtosis opcional) a partir de un vector 1D de intensidades [0..255]."""
    hist, prob, _ = histogram_and_prob(data, bins=256)
    stats = {
        "energia": energy(prob),
        "entropia": entropy(prob),
        "asimetria": skewness(data),
        "media": mean(data),
        "varianza": variance(data),
    }
    if include_kurtosis:
        stats["kurtosis"] = kurtosis_excess(data)
    return hist, prob, stats
