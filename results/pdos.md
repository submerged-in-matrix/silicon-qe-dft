# Projected Density of States (PDOS) Results

## Objective

Resolve the total density of states into orbital contributions (s and p) to understand the electronic structure and bonding in silicon.

---

## Key Results

- Lower valence band: stronger s-character
- Upper valence band: dominant p-character
- Conduction band: primarily p-like
- Spilling parameter: 0.009 (high-quality projection)

---

## Governing Equation

The projected density of states is:

PDOS(E) = Σ_{n,k} |⟨φ_i | ψ_{n,k}⟩|^2 δ(E - E_{n,k})

Where:
- φ_i = atomic orbital
- ψ_{n,k} = Kohn–Sham state

---

## Physical Interpretation

The PDOS reveals the orbital origin of electronic states:

- s and p contributions coexist across the valence region
- p orbitals dominate near the valence band maximum
- conduction states are also largely p-like

This distribution indicates that the electronic states are hybridized rather than purely atomic.

---

## Remarks

- Löwdin charge analysis shows ~3.96 electrons per Si atom
- s contribution ≈ 1.17, p contribution ≈ 2.79
- px, py, pz contributions are equal due to crystal symmetry
- small spilling parameter confirms reliability of projection

---

## Visualization

The PDOS plot includes:

- Total DOS
- s-projected DOS
- p-projected DOS

The plot shows:
- s contribution stronger at lower energies
- p contribution dominating near the valence band edge

![Projected DOS](si_pdos.png)

*Figure: Projected density of states showing orbital contributions. The valence band exhibits mixed s and p character, while p states dominate near the band edges, consistent with sp³ hybridization.*
