import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("si_charge_slice.dat")

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

x_unique = np.unique(x)
y_unique = np.unique(y)

Z = z.reshape(len(y_unique), len(x_unique))

plt.figure(figsize=(7, 6))
contour = plt.contourf(x_unique, y_unique, Z, levels=40)
plt.colorbar(contour, label="Charge density")
plt.xlabel("In-plane coordinate 1")
plt.ylabel("In-plane coordinate 2")
plt.title("2D Charge-Density Slice Through a Si–Si Bond")
plt.tight_layout()
plt.savefig("si_charge_slice.png", dpi=400, bbox_inches="tight")
plt.show()
