#one plot errors for each-type particle
#also it print latex-tables

import ROOT, numpy

#Use : from   Ostap.PyRoUts   import * # instead ostap.... if you use Bender
from ostap.histos.histos import h2_axes, h1_axis
from ostap.math.ve       import VE 

def complex_histo_draw(file_name, epidlc_val, epidsc_val, se1_val, se1_err, se0_val, se0_err, se2_val): 
 #from csv to numpy-array
 data = numpy.genfromtxt(file_name, delimiter = ',')
 srtformat="{:7.5f}";


 #binning
 y_bins  = [2.25, 2.75, 3.25, 3.75, 4.25]
 pt_bins = [ 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20 ]
 length_x = numpy.size(data, 0)

 #histogram for all bins
 hist_os = h2_axes( y_bins, pt_bins )

 #histograms with ratios & yeilds
 hist_y1 = h1_axis( pt_bins )
 hist_y2 = h1_axis( pt_bins )
 hist_y3 = h1_axis( pt_bins )
 hist_y4 = h1_axis( pt_bins )
 hist_array = [hist_y1, hist_y2, hist_y3, hist_y4]
 

 #filling loop
 pt_bin = 1
 y_bin  = 1
 for j in range(length_x - 1):
  if pt_bin == len(pt_bins):
   y_bin += 1
   pt_bin = 1
   print(str("\hline"))
   print("\multicolumn{6}{c}{$y\in$~(" + str(data[j + 1, 1]) + "," + str(data[j + 1, 2])+ ")}" + "\\" + "\\")
   print(str("\hline"))
  r    = data[j + 1, 13]/data[j + 1, 14]
  r_i  = data[j + 1, 18]/data[j + 1, 19]
  r_s  = data[j + 1, 20]/data[j + 1, 21]

  s1 = abs(r - r_s)
  s2 = abs(r - r_i)
  s3 = data[j + 1, 25]
  summ = (s1**2+s2**2+s3**2)**0.5
  bin_VE_1 = VE(summ, 0)

  #fill histogram with bins values
  bin_val = bin_VE_1

  #1. uncomment if one need to non-round-values
  hist_os.SetBinContent(y_bin, pt_bin, bin_val.value())
  hist_os.SetBinError(y_bin, pt_bin, bin_val.error())
  
  print("(" + str(data[j + 1, 3]) +"," + str(data[j + 1, 4]) + ") & "+ srtformat.format(r) + " & "+ srtformat.format(s1) + " & " + srtformat.format(s2) + " & " + srtformat.format(s3) + " & " + srtformat.format(summ)  +"\\" + "\\")
  #2. uncomment if one need to round-values
  #hist_os.SetBinContent(y_bin, pt_bin, round(bin_val.value()))
  #hist_os.SetBinError(y_bin, pt_bin, round(bin_val.error())) 

  #hist style
  #remove stat box
  hist_os.SetStats(0)
  #set z range
  hist_os.SetMinimum(0.)
  hist_os.SetMaximum(0.06)

  pt_bin += 1
 print("\n")
 return hist_os

def hist_design(hist, line_color):
 hist.SetLineColor(line_color)
 hist.SetMarkerSize(0.9)
 hist.SetMarkerColor(line_color)
 hist.SetMarkerStyle(4)
 hist.SetLineWidth(2)
 hist.GetXaxis().SetTitle(" P_{T}, GeV/c")
 hist.GetYaxis().SetTitle(" R, %")
 hist.SetTitle("Title")
 hist.SetStats(0)
 return hist


if __name__ == "__main__" :
 r_val_scpp = complex_histo_draw('data_scpp.csv', 13, 14, 18, 19, 20, 21, 25)
 r_val_sc0 = complex_histo_draw('data_sc0.csv', 13, 14, 18, 19, 20, 21, 25)

 h_canvas = ROOT.TCanvas("h1", "Bin_values", 1500, 600)
 h_canvas.Divide(2, 1)

 #bins hist
 h_canvas.cd(1)
 r_val_scpp.SetTitle("SCPP")
 r_val_scpp.Draw("text colz")

 h_canvas.cd(2)
 r_val_sc0.SetTitle("SC0")
 r_val_sc0.Draw("text colz")
 h_canvas.Update()
