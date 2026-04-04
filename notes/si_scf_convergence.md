# SCF Convergence Study for Silicon (Si)

## Objective

Solve the electronic ground state of bulk silicon using Density Functional Theory (DFT).

---

## Physical Model

many-electron Schrödinger equation approximation with the Kohn–Sham equations:

ρ(r) = Σ |ψ_i(r)|²

Ĥ ψ_i = ε_i ψ_i

Where:
- ρ(r): electron density
- ψ_i: Kohn–Sham orbitals
- ε_i: eigenvalues (energy levels)
- Ĥ: effective Hamiltonian (includes external, Hartree, and exchange-correlation terms)

---

## System Description

- Material: Silicon (Si)
- Crystal structure: Diamond cubic
- Atoms per unit cell: 2
- Pseudopotential: PBE (Perdew–Burke–Ernzerhof, a GGA functional)
- Method: Plane-wave basis + PAW (Projector Augmented Wave, a method that reconstructs accurate all-electron wavefunctions from smooth pseudo-wavefunctions by treating core and valence electrons efficiently within a plane-wave framework)

---

## Numerical Parameters

- ecutwfc = 40 Ry  
  → plane-wave kinetic energy cutoff  
- ecutrho = 320 Ry  
  → charge density cutoff (≈ 8× ecutwfc for PAW)  
- k-points = 6×6×6  
  → sampling of Brillouin zone (reciprocal space)  
- occupations = fixed  
  → appropriate for semiconductors  

---

## SCF Method

The SCF (Self-Consistent Field) procedure solves:

ρ_in → H[ρ] → ψ → ρ_out

until:

|ρ_out − ρ_in| < threshold

Convergence controlled by:

- conv_thr = 1.0×10⁻⁸ Ry  
- mixing_beta = 0.3 (density mixing factor)  
- diagonalization = conjugate gradient (robust solver)

---

## Results

- Total energy: -93.45138 Ry  
- SCF accuracy: < 7×10⁻⁸ Ry  
- Converged in 11 iterations  

---

## Physical Interpretation

The system has reached a self-consistent electron density such that:
- input and output densities match
- total energy is stable

This represents the **electronic ground state for the fixed crystal structure**.

---

## Notes

- Lower mixing_beta improved convergence stability  
- Conjugate gradient method avoided diagonalization instability  
