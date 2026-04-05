# Silicon_band_Structure DFT Workflow using Quantum ESPRESSO (functional used: PBE)

## Objective

Perform a complete Density Functional Theory (DFT) workflow for bulk silicon:
- obtain electronic ground state
- optimize crystal structure
- compute band structure
- extract band gap

---

## Workflow Overview

### 1. SCF (Self-Consistent Field)

Solved the Kohn–Sham equations to obtain the ground-state electron density:

Ĥ ψ_i = ε_i ψ_i

Key result:
- Total energy: -93.45138 Ry
- Converged electron density

---

### 2. Variable-Cell Relaxation (vc-relax)

Optimized atomic positions and lattice parameter by minimizing total energy:

F_i = -∂E/∂R_i  
σ = ∂E/∂cell  

Key result:
- Lattice parameter: ~5.47 Å
- Zero forces and stress (equilibrium structure)

---

### 3. Band Structure Calculation

Computed energy dispersion E(k) along high-symmetry path:

L → Γ → X → W → K

Key concepts:
- Bloch theorem
- Brillouin zone sampling

---

### 4. Band Gap Extraction

Band gap computed from:

Eg = E_CBM - E_VBM

Results:
- VBM ≈ 0 eV
- CBM ≈ 0.609 eV
- Band gap ≈ **0.61 eV**

---

## Physical Interpretation

- Silicon shows an **indirect band gap**
- VBM at Γ, CBM near X
- DFT (PBE) underestimates band gap (expected behavior)

---

## Project Structure
inputs/ → QE input files
outputs/ → raw QE outputs
pseudo/ → pseudopotentials
results/ → processed results and plots
notes/ → detailed technical notes


---

## Tools Used

- Quantum ESPRESSO (pw.x, bands.x)
- GNUplot (visualization)
- Bash utilities (awk, grep)

---

## Key Learnings

- SCF convergence control (mixing, diagonalization)
- Structural optimization using BFGS
- Reciprocal-space sampling and k-path selection
- Band gap extraction and interpretation
- Limitations of semi-local DFT (PBE)

---

## Future Work

- Compare LDA vs PBE vs hybrid functionals
- Density of States (DOS)
- Convergence studies (k-points, cutoff)

---

## Author

Md. Saidul Islam  
