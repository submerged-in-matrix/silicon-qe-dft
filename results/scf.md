# Silicon SCF Results

## Objective

Obtain the electronic ground-state energy for bulk silicon at a fixed lattice structure.

---

## Key Result

- Total energy: -93.45138 Ry  
- SCF accuracy: < 7×10⁻⁸ Ry  
- Number of iterations: 11  

---

## Governing Equation

The Kohn–Sham equation:

Ĥ ψ_i = ε_i ψ_i

Electron density:

ρ(r) = Σ |ψ_i(r)|²

Where:
- Ĥ: effective Hamiltonian
- ψ_i: electronic wavefunctions
- ε_i: energy eigenvalues
- ρ(r): electron density

---

## Energy Functional

Total energy is composed of:

E_total = T + E_ext + E_H + E_xc + E_ion-ion

Where:
- T: kinetic energy of electrons  
- E_ext: electron–nuclei interaction  
- E_H: Hartree energy (electron–electron Coulomb)  
- E_xc: exchange-correlation energy  
- E_ion-ion: ion–ion interaction (Ewald sum)

---

## Physical Meaning

The SCF solution gives:
- a stable electron density ρ(r)
- minimum total energy for the fixed atomic configuration

This is the **ground-state electronic structure**, but not yet the optimized geometry.

---

## Remarks

- Convergence achieved after stabilizing density mixing  
- Energy precision is sufficient for structural optimization  
