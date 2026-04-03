Day 1 — First SCF run (Si)

- QE installed and working
- Used PBE pseudopotential (PSLibrary)
- ecutwfc = 40 Ry
- k-points = 6x6x6
- SCF converged successfully
- Output saved in outputs/si_scf.out
Results:
- total energy              =     -93.44863752 Ry
- estimated scf accuracy    <       0.05479940 Ry
Issues faced:
- pseudo_dir path error (fixed by using ./pseudo/)
