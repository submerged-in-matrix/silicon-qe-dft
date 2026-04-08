# Silicon Electronic Structure DFT Workflow using Quantum ESPRESSO (PBE)

## Objective

Perform a complete Density Functional Theory (DFT) workflow for bulk silicon to:

- obtain the electronic ground state  
- optimize the crystal structure  
- compute band structure and density of states  
- extract and interpret the band gap  

---

## Workflow Overview

### 1. SCF (Self-Consistent Field)

Solved the Kohn–Sham equations to obtain the ground-state electron density:

Ĥ ψ_i = ε_i ψ_i  

**Key result:**
- Total energy: -93.45138 Ry  
- Converged electron density  

---

### 2. Variable-Cell Relaxation (vc-relax)

Optimized atomic positions and lattice parameter by minimizing total energy:

F_i = -∂E/∂R_i  
σ = ∂E/∂cell  

**Key result:**
- Lattice parameter: ~5.47 Å  
- Negligible forces and stress (equilibrium structure)  

---

### 3. Band Structure Calculation

Computed energy dispersion \(E(k)\) along the high-symmetry path:

L → Γ → X → W → K  

**Key concepts:**
- Bloch theorem  
- Brillouin zone sampling  

---

### 4. Band Gap Extraction

Band gap determined from:

Eg = E_CBM − E_VBM  

**Results:**
- VBM ≈ 0 eV (at Γ)  
- CBM ≈ 0.609 eV (along Γ–X)  
- Band gap ≈ **0.61 eV**  

---

### 5. Density of States (DOS)

Computed DOS using a dense k-point sampling (NSCF → dos.x).

**Key observations:**
- Valence band: high DOS below 0 eV  
- Band gap: region with D(E) ≈ 0  
- Conduction band: states above ~0.6 eV  

**Result:**
- DOS confirms band gap ≈ 0.6 eV  
- Consistent with band structure  

---

## Physical Interpretation

- Silicon exhibits an **indirect band gap semiconductor behavior**  
- Valence band maximum at Γ  
- Conduction band minimum along Γ–X  
- PBE-DFT underestimates band gap compared to experiment (~1.1 eV), as expected  

---

## Project Structure

inputs/ → Quantum ESPRESSO input files
outputs/ → raw calculation outputs
pseudo/ → pseudopotentials
results/ → processed plots and extracted results
notes/ → detailed physics and methodology notes


---

## Tools Used

- Quantum ESPRESSO (pw.x, bands.x, dos.x)  
- GNUplot (visualization)  
- Bash utilities (awk, grep)  

---

## Key Learnings

- SCF convergence control (mixing schemes, diagonalization methods)  
- Structural optimization using BFGS algorithm  
- k-space sampling and high-symmetry path selection  
- Extraction and validation of band gap  
- Complementary roles of band structure and DOS  
- Limitations of semi-local DFT (PBE)  

---

## Author

Md. Saidul Islam  
