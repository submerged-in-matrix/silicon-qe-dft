import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Option A: no energy shift
# 0 eV is only a visual reference
# ---------------------------------
FERMI = 0.0

# ---------------------------------
# input files
# ---------------------------------
total_file = "si.pdos_tot"
s1_file = "si.pdos_atm#1(Si)_wfc#1(s)"
s2_file = "si.pdos_atm#2(Si)_wfc#1(s)"
p1_file = "si.pdos_atm#1(Si)_wfc#2(p)"
p2_file = "si.pdos_atm#2(Si)_wfc#2(p)"

# ---------------------------------
# read data
# ---------------------------------
total_data = np.loadtxt(total_file, comments="#")
s1_data = np.loadtxt(s1_file, comments="#")
s2_data = np.loadtxt(s2_file, comments="#")
p1_data = np.loadtxt(p1_file, comments="#")
p2_data = np.loadtxt(p2_file, comments="#")

energy = total_data[:, 0] - FERMI
total_dos = total_data[:, 1]
s_total = s1_data[:, 1] + s2_data[:, 1]
p_total = p1_data[:, 1] + p2_data[:, 1]

# ---------------------------------
# plot
# ---------------------------------
plt.figure(figsize=(8.5, 6.2))

plt.plot(energy, total_dos, linewidth=2.4, label="Total DOS")
plt.plot(energy, s_total, linewidth=2.0, label="Si s-PDOS")
plt.plot(energy, p_total, linewidth=2.0, label="Si p-PDOS")

plt.axvline(0.0, linestyle="--", linewidth=1.2, label="0 eV reference")
plt.axhline(0.0, color="black", linewidth=0.8)

plt.xlabel("Energy (eV)")
plt.ylabel("DOS (states/eV)")
plt.title("Projected Density of States (PDOS) of Silicon")

plt.xlim(-6.5, 16.0)
plt.ylim(0, max(total_dos) * 1.08)

plt.legend(frameon=False, loc="upper right")
plt.tight_layout()

plt.savefig("silicon_pdos_clean.png", dpi=400, bbox_inches="tight")
plt.show()