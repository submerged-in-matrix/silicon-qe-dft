import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("dft_data/si_dos.dat", comments="#")

energy = data[:, 0]
dos = data[:, 1]

plt.figure(figsize=(8, 6))
plt.plot(energy, dos, linewidth=2, label="DOS")
plt.axhline(0.0, color="black", linewidth=0.8)
plt.axvline(0.0, linestyle="--", linewidth=1.2, label="0 eV reference")

plt.xlabel("Energy (eV)")
plt.ylabel("DOS (states/eV)")
plt.title("Density of States of Silicon")
plt.legend(frameon=False)
plt.ylim(bottom=0)
plt.tight_layout()

plt.savefig("results/si_dos.png", dpi=400, bbox_inches="tight")
plt.show()
