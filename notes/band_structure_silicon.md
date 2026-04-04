# Band Structure Calculation for Silicon

## Objective

Determine the electronic band structure of silicon to understand its energy dispersion and band gap.

---

## Physical Concept

In a periodic crystal, electrons experience a periodic potential:

V(r + R) = V(r)

This leads to Bloch’s theorem:

ψ_{n,k}(r) = e^{i k·r} u_{n,k}(r)

Where:
- k: wavevector in reciprocal space
- n: band index
- u_{n,k}(r): periodic function

---

## What is Band Structure?

Band structure describes how electron energy varies with k:

E = E_n(k)

It shows:
- allowed energy levels (bands)
- forbidden regions (band gaps)

---

## Brillouin Zone

- The Brillouin zone is the primitive cell in reciprocal space
- Electronic properties are determined by sampling k-points within it

For silicon (FCC lattice), important high-symmetry points include:
- Γ (Gamma)
- X
- L
- K

Band structure is plotted along paths connecting these points.

---

## Method

Band structure calculation involves:

1. Perform SCF → obtain ground-state charge density ρ(r)
2. Perform non-SCF (NSCF) calculation along high-symmetry k-path
3. Solve Kohn–Sham equations for fixed ρ(r)

---

## Governing Equation

Kohn–Sham equation:

Ĥ ψ_{n,k} = E_{n,k} ψ_{n,k}

Where:
- E_{n,k}: energy of band n at k-point
- ψ_{n,k}: wavefunction

---

## Key Concepts

### Valence Band
- Highest occupied band at T = 0 K

### Conduction Band
- Lowest unoccupied band

### Band Gap

E_g = E_conduction − E_valence

---

## Silicon Band Structure

- Indirect band gap semiconductor
- Valence band maximum at Γ
- Conduction band minimum near X

---

## Numerical Considerations

- Dense k-path needed for smooth bands
- Same ecutwfc and pseudopotential as SCF
- NSCF uses fixed charge density (no mixing)

---

## Physical Interpretation

Band structure reveals:
- electronic transport properties
- semiconductor vs metal behavior
- optical transitions

---

## Choice of k-Path (High-Symmetry Points)

The band structure is evaluated along a path connecting high-symmetry points in the Brillouin zone of an FCC lattice.

Selected path:

L → Γ → X → W → K

Coordinates (in reciprocal lattice units):

- L = (0.5, 0.5, 0.5)
- Γ = (0.0, 0.0, 0.0)
- X = (0.5, 0.0, 0.5)
- W = (0.625, 0.25, 0.625)
- K = (0.375, 0.375, 0.75)

These points are chosen because:
- they represent symmetry boundaries of the Brillouin zone
- band extrema and degeneracies occur here
- they reveal key features such as the band gap

For silicon:
- valence band maximum occurs at Γ
- conduction band minimum occurs near X

→ This confirms silicon as an **indirect band gap semiconductor**

---

## Remarks

- PBE underestimates band gap (known limitation)
- More accurate methods: GW, hybrid functionals
