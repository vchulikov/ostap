import ROOT, numpy
from ostap.histos.histos import h2_axes, h1_axis
from ostap.math.ve       import VE 

def complex_histo_draw(file_name, val_1_col, err_1_col, val_2_col, err_2_col, val_3_col, err_3_col, val_4_col, err_4_col): 
 #from csv to numpy-array
 data = numpy.genfromtxt(file_name, delimiter = ',')
 
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
  bin_VE_1 = VE(data[j + 1, val_1_col], data[j + 1, err_1_col]**2)
  bin_VE_2 = VE(data[j + 1, val_2_col], data[j + 1, err_2_col]**2)
  bin_VE_3 = VE(data[j + 1, val_3_col], data[j + 1, err_3_col]**2)
  bin_VE_4 = VE(data[j + 1, val_4_col], data[j + 1, err_4_col]**2)

  #fill histogram with bins values
  bin_val = bin_VE_2*bin_VE_4/(bin_VE_1*bin_VE_3)

  #1. uncomment if one need to non-round-values
  hist_os.SetBinContent(y_bin, pt_bin, bin_val.value())
  hist_os.SetBinError(y_bin, pt_bin, bin_val.error())
  
  #2. uncomment if one need to round-values
  #hist_os.SetBinContent(y_bin, pt_bin, round(bin_val.value()))
  #hist_os.SetBinError(y_bin, pt_bin, round(bin_val.error())) 
  
  #stuff for changing bin's colors which determine by Z axis range in 2d hist
  #hist_os.SetMinimum(0.)
  #hist_os.SetMaximum(0.08)
  
  #fill histogram with R-values
  hist_array[y_bin - 1].SetBinContent(pt_bin, 100*(bin_val.value()))
  hist_array[y_bin - 1].SetBinError(pt_bin, 100*(bin_val.error()))

  pt_bin += 1

 return hist_os, hist_array[0], hist_array[1], hist_array[2], hist_array[3]

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
 r_val, h_y1, h_y2, h_y3, h_y4 = complex_histo_draw('data_nominal.csv', 5, 6, 7, 8, 9, 10, 11, 12)

 h_canvas = ROOT.TCanvas("h1", "Bin_values", 1500, 600)
 h_canvas.Divide(2, 1)

 legend = ROOT.TLegend(0.9, 0.7, 0.7, 0.8)
 
 h_canvas.cd(2)
 #hists design
 bin_y1 = hist_design(h_y4, 2)
 bin_y2 = hist_design(h_y3, 3)
 bin_y3 = hist_design(h_y2, 4)
 bin_y4 = hist_design(h_y1, 6)
 
 #draw
 bin_y1.Draw("e1")
 bin_y2.Draw("same e1")
 bin_y3.Draw("same e1")
 bin_y4.Draw("same e1")

 #legend
 legend.AddEntry(bin_y1, "3.75 < y < 4.25")
 legend.AddEntry(bin_y2, "3.25 < y < 3.75")
 legend.AddEntry(bin_y3, "2.75 < y < 3.25")
 legend.AddEntry(bin_y4, "2.25 < y < 2.75")
 legend.SetBorderSize(0)
 legend.Draw()

 #bins hist
 h_canvas.cd(1)
 r_val.Draw("text e col")
 h_canvas.Update()
