##pt + R PID + s1 + s2 + s3 + summ_err --->latex table
import numpy

if __name__ == "__main__" :
 data = numpy.genfromtxt('data_all.csv', delimiter = ',')
 length_x = numpy.size(data, 0)
 srtformat="{:7.5f}";

 for i in range(length_x - 1):
  r = data[i + 1, 15]/data[i + 1, 16] #13, 14 in old-type data-file
  s1 = abs(r - data[i + 1, 20]/data[i + 1, 21]) #15, 16 in old-type data-file
  s2 = abs(r - data[i + 1, 18]/data[i + 1, 19])
  s3 = data[i + 1, 25]
  summ_err = (s1**2+s2**2+s3**2)**0.5
  
  if i%10 == 0: 
   print(str("\hline"))
   print("\multicolumn{6}{c}{$y\in$~(" + str(data[i + 1, 1]) + "," + str(data[i + 1, 2])+ ")}" + "\\" + "\\")
   print(str("\hline"))
  print("(" + str(data[i + 1, 3]) +"," + str(data[i + 1, 4]) + ") & "+ srtformat.format(r) + " & "+ srtformat.format(s1) + " & " + srtformat.format(s2) + " & " + srtformat.format(s3) + " & " + srtformat.format(summ_err)  +"\\" + "\\")
