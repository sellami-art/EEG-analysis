import numpy as np
import matplotlib.pyplot as plt

# Générer des données EEG simulées (onde sinusoïdale + bruit)
fs = 250  # fréquence d'échantillonnage (Hz)
t = np.arange(0, 2, 1/fs)  # 2 secondes
freq = 10  # fréquence de la sinusoïde (Hz)

signal = np.sin(2 * np.pi * freq * t) + 0.5 * np.random.randn(len(t))

# Calculs simples
mean_val = np.mean(signal)
var_val = np.var(signal)

print(f"Moyenne du signal EEG simulé : {mean_val:.3f}")
print(f"Variance du signal EEG simulé : {var_val:.3f}")

# Tracé
plt.plot(t, signal)
plt.title("Signal EEG simulé")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.show()
