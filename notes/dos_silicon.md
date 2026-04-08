# Density of States (DOS) Calculation for Silicon

## Objective

Compute the Density of States (DOS) of silicon to understand the distribution of electronic states as a function of energy and to confirm the band gap obtained from band structure calculations.

---

## Physical Concept

The Density of States is defined as:

D(E) = Σ_{n,k} δ(E - E_{n,k})

Where:
- E = energy
- E_{n,k} = eigenvalue of band n at k-point k
- δ = Dirac delta function

---

## Interpretation

D(E) represents the number of available electronic states per energy interval.

- High DOS → many states available
- Low DOS → few states
- D(E) = 0 → no allowed states (band gap)

---

## Methodology

### Step 1: SCF (already performed)

Obtain converged charge density ρ(r).

---

### Step 2: NSCF Calculation

Perform Non-Self-Consistent Field (NSCF) calculation using a dense k-point mesh:

- Uses fixed charge density from SCF
- Computes eigenvalues on a fine grid in reciprocal space

Input highlights:
- calculation = 'nscf'
- k-points = 12 × 12 × 12
- nbnd = 24 (includes unoccupied states)

Purpose:
- ensure sufficient sampling of E_{n,k}
- include conduction band states

---

### Step 3: DOS Calculation (dos.x)

Compute DOS from NSCF eigenvalues.

Key input parameters:

- prefix = 'si'  
- outdir = './tmp/'  
- fildos = 'si_dos.dat'  
- Emin = -6.0 eV  
- Emax = 4.0 eV  
- DeltaE = 0.01 eV  

Smoothing:
- ngauss = 0 (Gaussian smearing)
- degauss = 0.02 eV

---

## Output File Structure

si_dos.dat contains:

Column 1: Energy (eV)  
Column 2: DOS (states/eV)  
Column 3: Integrated DOS  

Header includes:
- Fermi energy (EFermi)

---

## Key Results

From the DOS plot:

### Valence Band
- Energy range: ~−6 eV to ~0 eV
- High DOS → occupied states

### Band Gap
- Region with D(E) ≈ 0
- Width ≈ 0.6 eV

### Conduction Band
- Starts above ~0.6 eV
- Represents unoccupied states

---

## Band Gap Confirmation

Band gap from DOS:

Eg ≈ 0.6 eV

This matches the value obtained from band structure calculations.

---

## Physical Interpretation

- Silicon is a semiconductor with a clear gap in DOS
- DOS confirms absence of electronic states in the band gap region
- Peaks in DOS correspond to flat bands (low dispersion)
- Low DOS regions correspond to dispersive bands

---

## Important Considerations

### 1. Number of Bands (nbnd)
- Must include sufficient unoccupied states
- Otherwise conduction band will be missing

---

### 2. k-point Sampling
- Dense grid required (e.g., 12×12×12)
- Poor sampling leads to noisy DOS

---

### 3. Smearing (degauss)
- Controls smoothness of DOS
- Too small → noisy spikes
- Too large → over-smoothed features

---

## Comparison with Band Structure

| Quantity | Band Structure | DOS |
|--------|--------------|-----|
| Shows | E(k) | D(E) |
| Reveals | dispersion | state density |
| Gap type | direct/indirect | only gap size |

---

## Limitations

- DOS does not reveal k-dependent information
- Cannot distinguish direct vs indirect band gap
- Depends on chosen smearing and k-grid

---

## Conclusion

The DOS calculation confirms the semiconducting nature of silicon with a band gap of approximately 0.6 eV, consistent with band structure results. The combination of DOS and band structure provides a complete electronic description of the system.
