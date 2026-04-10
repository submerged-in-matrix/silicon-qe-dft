# Projected Density of States (PDOS) Calculation for Silicon

## Objective

Compute the Projected Density of States (PDOS) of silicon to identify the orbital contributions to the electronic states and to understand the bonding character of the valence and conduction bands.

---

## Physical Concept

The Density of States gives the number of available states at each energy.

The Projected Density of States decomposes the total DOS into contributions from specific atomic orbitals:

PDOS(E) = Σ_{n,k} |⟨φ_i | ψ_{n,k}⟩|^2 δ(E - E_{n,k})

Where:
- φ_i = atomic-like orbital used for projection
- ψ_{n,k} = Kohn–Sham eigenstate
- E_{n,k} = eigenvalue of band n at k-point k
- δ = Dirac delta function

---

## Interpretation

PDOS reveals which orbitals contribute to different energy regions.

For silicon:
- s states contribute more strongly in the lower valence region
- p states dominate near the top of the valence band
- conduction states are also largely p-like

This helps connect the electronic structure to chemical bonding.

---

## Methodology

### Step 1: SCF (already performed)

Obtain converged ground-state charge density ρ(r).

---

### Step 2: NSCF Calculation (already performed)

Use a dense k-point mesh to compute eigenvalues and eigenvectors on a fine grid in reciprocal space.

Purpose:
- improve energy sampling
- include unoccupied states
- provide wavefunctions for projection analysis

---

### Step 3: PDOS Calculation (projwfc.x)

Run `projwfc.x` using the NSCF output.

Input highlights:
- prefix = 'si'
- outdir = './tmp/'
- DeltaE = 0.01
- degauss = 0.02
- ngauss = 0

Purpose:
- project Kohn–Sham states onto atomic-like orbitals
- resolve total DOS into orbital contributions
- compute Löwdin charges and spilling parameter

---

## Output File Structure

The PDOS calculation generates several files.

### Main output
`si.pdos.out`

Contains:
- projection information
- atomic states used for projection
- orbital decomposition of selected eigenstates
- Löwdin charges
- spilling parameter

---

### Total projected DOS
`si.pdos_tot`

Columns:
- Column 1: Energy (eV)
- Column 2: total DOS
- Column 3: total projected DOS

---

### Orbital-resolved PDOS files

Examples:
- `si.pdos_atm#1(Si)_wfc#1(s)`
- `si.pdos_atm#2(Si)_wfc#1(s)`
- `si.pdos_atm#1(Si)_wfc#2(p)`
- `si.pdos_atm#2(Si)_wfc#2(p)`

#### s-file
Columns:
- Column 1: Energy (eV)
- Column 2: ldos(E)
- Column 3: pdos(E)

Since s has only one angular component, ldos(E) and pdos(E) are identical.

#### p-file
Columns:
- Column 1: Energy (eV)
- Column 2: ldos(E)
- Columns 3–5: individual p components

The p-file contains three components corresponding to the three p orbitals.

---

## Projection Basis

For the 2-atom silicon primitive cell, the atomic states used for projection are:

- atom 1: one s state + three p states
- atom 2: one s state + three p states

Total number of projection states:

natomwfc = 8

This is consistent with the valence orbital channels of silicon used in the pseudopotential.

---

## Key Results

### Total DOS vs Projected DOS
- The projected DOS closely matches the total DOS
- This indicates that the chosen atomic projection basis captures the electronic states well

---

### Orbital Character

From the PDOS plot:

#### Lower Valence Region
- stronger s contribution
- mixed with p character

#### Upper Valence Region
- dominated by p states
- corresponds to the top of the valence band

#### Conduction Region
- primarily p-like
- with smaller s contribution

---

## Löwdin Charge Analysis

From `si.pdos.out`:

For each Si atom:
- total charge ≈ 3.9642
- s contribution ≈ 1.1741
- p contribution ≈ 2.7901

The p charge is equally distributed among px, py, and pz:

- px ≈ 0.9300
- py ≈ 0.9300
- pz ≈ 0.9300

This reflects the symmetry of bulk silicon.

---

## Spilling Parameter

Spilling parameter:

0.0090

Interpretation:
- measures how much of the Kohn–Sham states is not captured by the projection basis
- small value indicates high-quality projection

Thus, the PDOS analysis is reliable.

---

## Physical Interpretation

The PDOS shows that the electronic states in silicon are not purely s or purely p.

Instead:
- lower valence states contain stronger s character
- upper valence and conduction states are dominated by p character
- both contributions coexist across the bonding region

This is consistent with **sp³ hybridization** in diamond-structure silicon.

---

## Important Considerations

### 1. NSCF Quality
- PDOS depends on a sufficiently dense k-point mesh
- poor sampling leads to noisy orbital-resolved spectra

---

### 2. Number of Bands
- must include enough unoccupied states
- otherwise conduction-band PDOS will be incomplete

---

### 3. Smearing
- degauss controls smoothness of the PDOS curves
- too small → noisy peaks
- too large → broad, less resolved features

---

### 4. Projection Basis
- PDOS depends on the atomic-like orbitals provided by the pseudopotential
- projection is approximate, not exact
- this is why the spilling parameter is important

---

## Comparison with Total DOS

| Quantity | DOS | PDOS |
|--------|-----|------|
| Shows | total state density | orbital-resolved state density |
| Reveals | where states exist in energy | which orbitals contribute |
| Bonding insight | limited | strong |

---

## Limitations

- PDOS depends on the projection scheme
- orbital decomposition is basis-dependent
- does not directly show real-space charge distribution
- energy reference here is not aligned to the Fermi level because fixed occupations were used

---

## Conclusion

The PDOS calculation reveals the orbital origin of the electronic states in silicon. The lower valence region contains stronger s contribution, while the upper valence and much of the conduction region are dominated by p character. This orbital mixing confirms the hybridized bonding nature of silicon and supports the sp³ bonding picture of the diamond cubic structure.