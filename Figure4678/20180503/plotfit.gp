set datafile separator ","

set xlabel "Velocity (mm/min)"
set ylabel "Force (N)"
set xrange [0:1800]
#set yrange [0.13:0.25]

#a1=0.0633
#b1=0.005092
#c1=0.155
#f1(x)=a1*exp(-b1*x)+c1
#fit f1(x) 'maxs.csv' u 1:2 via a1,b1,c1

#plot 'maxs.csv' using 1:2 title '41'  with lines,\
#f1(x) title sprintf('%.2f *e^(- %.2f x)+%.2f', a1,b1,c1)

#a2=0.0633
#b2=0.005092
#c2=0.155
#f2(x)=a2*exp(-b2*x)+c2
#fit f2(x) 'maxs.csv' u 1:3 via a2,b2,c2

#plot 'maxs.csv' using 1:3 title '53'  with lines,\
#f2(x) title sprintf('%.2f *e^(- %.2f x)+%.2f', a2,b2,c2)

#a3=0.05331
#b3=0.002212
#c3=0.169842482
#f3(x)=a3*exp(-b3*x)+c3
#fit f3(x) 'maxs.csv' u 1:4 via a3,b3,c3

#plot 'maxs.csv' using 1:4 title '65'  with lines,\
#f3(x) title sprintf('%.2f *e^(- %.2f x)+%.2f', a3,b3,c3)

a4=0.0886057
b4=0.0062952182
c4=0.195314914
f4(x)=a4*exp(-b4*x)+c4
fit f4(x) 'maxs.csv' u 1:5 via a4,b4,c4

plot 'maxs.csv' using 1:5 title '77'  with lines,\
f4(x) title sprintf('%.2f *e^(- %.2f x)+%.2f', a4,b4,c4)

#a8=0.0633
#b8=0.005092
#c8=0.155
#f8(x)=a8*exp(-b8*x)+c8
#fit f8(x) 'maxs.csv' u 1:9 via a8,b8,c8


#plot 'maxs.csv' using 1:2 title '41'  with lines,\
#'maxs.csv' using 1:3 title '53'  with lines,\
#'maxs.csv' using 1:4 title '65'  with lines,\
#'maxs.csv' using 1:5 title '77'  with lines,\
#'maxs.csv' using 1:6 title '89'  with lines,\
#'maxs.csv' using 1:7 title '184'  with lines,\
#'maxs.csv' using 1:8 title '232'  with lines#,\
#f8(x) title sprintf('%.2f *e^(- %.2f x)+%.2f', a8,b8,c8)

pause -1
