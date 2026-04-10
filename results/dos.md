# Density of States (DOS) Results

## Objective

Compute the Density of States (DOS) of silicon and confirm the band gap obtained from band structure calculations.

---

## Key Results

- Band gap (Eg): ~0.6 eV
- Valence band: populated states below 0 eV
- Conduction band: states begin above ~0.6 eV

---

## Governing Equation

The Density of States is defined as:

D(E) = Σ_{n,k} δ(E - E_{n,k})

Where:
- E = energy
- E_{n,k} = eigenvalue of band n at k-point k

---

## Physical Interpretation

The DOS shows the distribution of electronic states as a function of energy.

From the plot:

- High DOS in the valence region indicates many occupied states
- A clear region with D(E) ≈ 0 confirms the band gap
- The conduction band begins above the gap with available unoccupied states

---

## Remarks

- The DOS confirms the indirect band gap obtained from band structure
- Smearing (degauss = 0.02 eV) ensures smooth curves
- Dense k-point sampling is essential for accurate DOS

---

## Visualization

The DOS is computed from NSCF eigenvalues and plotted as a function of energy.

Energy is referenced relative to the chosen zero (not explicitly aligned to Fermi level due to fixed occupations).

The plot shows:
- clear separation between valence and conduction bands
- absence of states in the band gap region

![Density of States](si_dos.png)

*Figure: Density of states of silicon showing a clear band gap (~0.6 eV) separating valence and conduction bands.*
