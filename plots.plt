set term png
set output "trans_muestra2.png"

set title "Transición Mecánico-Difusora para la Muestra I"
set xlabel "Tiempo(s)"
set ylabel "Presion (Torr)"

set xrange[100:2000]
plot "MuestraI_difu.txt" title "P(t)" pt 16 lc rgb 'orange' 

set term aqua
plot "MuestraI_difu.txt" title "P(t)" pt 16 lc rgb 'orange' 

