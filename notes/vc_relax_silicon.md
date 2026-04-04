# Variable-Cell Relaxation (vc-relax) for Silicon

## Objective

Determine the equilibrium crystal structure of silicon by minimizing total energy with respect to both atomic positions and lattice parameters.

---

## Physical Model

The total energy depends on:

E = E({R_i}, cell)

Where:
- R_i: atomic positions
- cell: lattice vectors (shape and volume)

The equilibrium structure satisfies:

F_i = -∂E/∂R_i = 0  
σ = ∂E/∂cell = 0  

Where:
- F_i: force on atom i  
- σ: stress tensor  

---

## Method

The vc-relax calculation performs:

1. SCF → solve electronic structure  
2. Compute forces and stress  
3. Update atomic positions and cell  
4. Repeat until convergence  

Optimization algorithm:
- BFGS (Broyden–Fletcher–Goldfarb–Shanno)
  - is a quasi-Newton optimization method that uses forces (energy gradients) to iteratively move atoms and adjust the cell toward lower energy, 
  - while building an approximate curvature (second-derivative) of the energy surface to accelerate convergence compared to simple gradient descent.
---

## Key Parameters

- calculation = vc-relax  
  → relax atoms + cell  
- ion_dynamics = bfgs  
  → atomic position optimization  
- cell_dynamics = bfgs  
  → lattice optimization  
- press = 0.0  
  → target pressure (kbar)  
- forc_conv_thr = 1.0×10⁻³ Ry/Bohr  
  → force convergence threshold  
- press_conv_thr = 0.5 kbar  
  → stress convergence threshold  

---

## Results Summary

- BFGS steps: 3  
- SCF cycles: 4  
- Final energy: -93.45182 Ry  

---

## Physical Interpretation

The system reached equilibrium when:
- forces on atoms vanished  
- internal stress became zero  
- total energy reached minimum  

This gives the **ground-state crystal structure** of silicon.

---

## Remarks

- Atomic positions remained unchanged due to symmetry  
- Only lattice parameter adjusted  
- PBE functional slightly overestimates lattice constant (expected behavior)  
