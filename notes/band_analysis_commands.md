# Band Analysis Commands

## 1. Find highest occupied level from previous outputs

```bash
grep -R "highest occupied level" outputs/

# compute VBM, CBM and Band gap
awk 'BEGIN{Ef=5.9846; v=-1e9; c=1e9}
     NF>=2 {
         e=$2-Ef;
         if (e<=0 && e>v) v=e;
         if (e>0  && e<c) c=e;
     }
     END{
         printf "VBM = %.6f eV\n", v;
         printf "CBM = %.6f eV\n", c;
         printf "Eg  = %.6f eV\n", c-v;
     }' si_bands.dat.gnu

# Find x-positions of high-symmetry points from the first band block
awk 'NF==0{exit} NR==1 || NR==21 || NR==41 || NR==61 || NR==81 {print NR, $1}' si_bands.dat.gnu

# Plotting bandgap
Ef = 5.9846

set terminal qt size 1100,750
set title "Silicon Band Structure"
set xlabel "High-symmetry k-path"
set ylabel "Energy - E_F (eV)"

set key off
set grid ytics
set xrange [0:2.8108]
set yrange [-6:4]

set xtics ("L" 0.0000, "{/Symbol G}" 0.8596, "X" 1.8521, "W" 2.2030, "K" 2.8108)

# Fermi reference
set arrow 1 from 0,0 to 2.8108,0 nohead dt 2 lw 1

# symmetry separators
set arrow 2 from 0.8596,-6 to 0.8596,4 nohead dt 3 lw 1
set arrow 3 from 1.8521,-6 to 1.8521,4 nohead dt 3 lw 1
set arrow 4 from 2.2030,-6 to 2.2030,4 nohead dt 3 lw 1

# VBM and CBM markers
set label 1 "VBM ({/Symbol G})" at 0.62,0.35
set arrow 5 from 0.70,0.28 to 0.8596,-0.0001 nohead lw 1

set label 2 "CBM" at 1.95,1.05
set arrow 6 from 1.93,0.95 to 1.7032,0.6093 nohead lw 1

# indirect band gap arrow
set label 3 "Indirect band gap" at 1.10,1.45
set arrow 7 from 0.8596,-0.0001 to 1.7032,0.6093 heads lw 1

plot "si_bands.dat.gnu" using 1:($2-Ef) w l
