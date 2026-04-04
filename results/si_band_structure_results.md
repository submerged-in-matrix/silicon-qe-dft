# Silicon Band Structure Results

## Objective

Compute the electronic band structure of silicon and determine the band gap.

---

## Key Results

- Valence Band Maximum (VBM): -0.0001 eV
- Conduction Band Minimum (CBM): 0.6093 eV
- Band gap (Eg): 0.6094 eV

---

## Governing Equation

The band gap is defined as:

Eg = ECBM - EVBM

Where:
- ECBM: energy of the conduction band minimum
- EVBM: energy of the valence band maximum

---

## Physical Interpretation

The calculation shows that silicon is a semiconductor with an indirect band gap.

This means:
- the top of the valence band and the bottom of the conduction band occur at different k-points
- an electron transition across the gap involves a change in crystal momentum

---

## Remarks

- The DFT-PBE band gap is smaller than the experimental value (~1.1 eV)
- This underestimation is a known limitation of semi-local exchange-correlation functionals such as PBE
- The qualitative band topology is correct

---

## Visualization

The band structure is plotted along the high-symmetry path:

L → Γ → X → W → K

Energy is referenced to the Fermi level (E_F = 0 eV).

The plot clearly shows:
- valence band maximum at Γ
- conduction band minimum near X
- indirect band gap

See: si_band_structure_final.png
