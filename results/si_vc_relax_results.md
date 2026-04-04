# Silicon vc-relax Results

## Objective

Obtain the equilibrium lattice parameter and optimized structure of silicon.

---

## Final Results

- Lattice parameter (a₀): 5.47 Å  
- Total energy: -93.45182 Ry  
- Volume: 40.92 Å³  
- Density: 2.279 g/cm³  

---

## Convergence

- BFGS converged in 3 steps  
- SCF converged at each step  
- Forces ≈ 0 Ry/Bohr  
- Pressure ≈ 0 kbar  

---

## Governing Equations

Force:

F_i = -∂E/∂R_i  

Stress:

σ = ∂E/∂cell  

Equilibrium condition:

F_i = 0 and σ = 0  

---

## Physical Meaning

- Atoms experience no net force → stable positions  
- Cell experiences no pressure → equilibrium volume  
- Energy is minimized → ground-state structure  

---

## Interpretation

The optimized lattice constant is slightly larger than experimental value (~5.43 Å), which is a known characteristic of the PBE exchange-correlation functional.

---

## Key Insight

Structural optimization is essential before further calculations (e.g., band structure), because electronic properties depend strongly on lattice geometry.
