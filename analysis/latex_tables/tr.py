#table 8 ---> | pt | eff_lc/eff_scpp | sE1 | sE0 | sE2 |
import numpy
if __name__ == "__main__" :
 data = numpy.genfromtxt('data_all.csv', delimiter = ',')
 length_x = numpy.size(data, 0)
 srtformat="{:7.2f}";

 for i in range(length_x - 1):
  r = data[i + 1, 13]/data[i + 1, 14]
  se1_val = data[i + 1, 36]
  se1_err = data[i + 1, 37]
  se0 = data[i + 1, 38]
  se2 = data[i + 1, 40]
  if i%10 == 0: 
   print(str("\hline"))
   print("\multicolumn{5}{c}{$y\in$~(" + str(data[i + 1, 1]) + "," + str(data[i + 1, 2])+ ")}" + "\\" + "\\")
   print(str("\hline"))
  print("(" + str(data[i + 1, 3]) +"," + str(data[i + 1, 4]) + ") & " + srtformat.format(r) + " & " + srtformat.format(se1_val)+ "~$\pm$  " + srtformat.format(se1_err) +" & " + srtformat.format(se0) + " & " + srtformat.format(se2) + " & " + srtformat.format((se1_err**2 + (r-se2)**2)**0.5) +"\\" + "\\" )
