import numpy
from ROOT import TCanvas, TLegend
from ostap.histos.histos import h2_axes, h1_axis
from ostap.math.ve       import VE 

def complex_histo_draw(file_name, val_1_col, err_1_col, val_2_col, err_2_col, corr_1_val): 
 #from csv to numpy-array
 data = numpy.genfromtxt(file_name, delimiter = ',')
 
 #binning
 #for statistic
 y_bins_1  = [2.25, 2.75, 3.25, 3.75, 4.25]
 pt_bins_1 = [ 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20 ]
 #for systematic
 y_bins_2  = [2.25, 2.75, 3.25, 3.75, 4.25]
 pt_bins_2 = [ 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20 ]
 length_x = numpy.size(data, 0)

 #histograms with ratios & yeilds
 #stat
 hist_array_1 = [h1_axis(pt_bins_1), h1_axis(pt_bins_1), h1_axis(pt_bins_1), h1_axis(pt_bins_1)]
 #syst
 hist_array_2 = [h1_axis(pt_bins_2), h1_axis(pt_bins_2), h1_axis(pt_bins_2), h1_axis(pt_bins_2)]

 #filling loop
 pt_bin = 1
 y_bin  = 1
 for j in range(length_x - 1):
  if pt_bin == len(pt_bins_1):
   y_bin += 1
   pt_bin = 1 
  bin_VE_1 = VE(data[j + 1, val_1_col]*data[j+1, corr_1_val], (data[j + 1, val_1_col]*data[j + 1, err_1_col])**2) #R + syst
  bin_VE_2 = VE(data[j + 1, val_2_col]*data[j+1, corr_1_val], (data[j + 1, val_2_col]*data[j + 1, err_2_col])**2) #R + stat

  #fill histogram with bins values
  #syst
  bin_val_1 = bin_VE_1
  #stat
  bin_val_2 = bin_VE_2

  #fill histogram with R-values
  hist_array_1[y_bin - 1].SetBinContent(pt_bin, bin_val_1.value())
  hist_array_1[y_bin - 1].SetBinError(pt_bin, bin_val_1.error())

  hist_array_2[y_bin - 1].SetBinContent(pt_bin, bin_val_2.value())
  hist_array_2[y_bin - 1].SetBinError(pt_bin, bin_val_2.error())

  pt_bin += 1
 return hist_array_1[0], hist_array_2[0]

def hist_design(hist, line_color):
 hist.SetLineColor(line_color)
 hist.SetMarkerSize(0.9)
 hist.SetMarkerColor(line_color)
 hist.SetMarkerStyle(4)
 hist.SetLineWidth(1)#2
 hist.GetXaxis().SetTitle(" P_{T}, GeV/c")
 hist.GetYaxis().SetTitle(" R, barn*somthing else")
 hist.SetTitle("Cross-section")
 hist.SetStats(0)
 return hist

if __name__ == "__main__" :
 h_y1, h_y2= complex_histo_draw('data_file.csv', 14, 15, 14, 16, 17) #14 - R-val, 15 - stat. err., 16 - syst.err., 17 - corr.f

 h_canvas = TCanvas("h1", "Bin_values", 1500, 600)

 bin_y2 = hist_design(h_y1, 419)
 bin_y1 = hist_design(h_y2, 419)

 #draw
 h_y2.Draw("e1")
 h_y1.Draw("same e1")

 #add legend
 legend = TLegend(0.9, 0.7, 0.7, 0.8)
 legend.AddEntry(bin_y1, "initial value < y < final value") #hist_array_1[0] - 2.25 - 2.75, hist_array_1[1] - 2.75...
 legend.SetBorderSize(0)
 legend.Draw()

 h_canvas.Update()
