from ROOT import *
import ostap.fitting.models as Models
#import ostap.fitting.basic as Am

#data-file

input_file = TFile.Open("db.root", 'read')
input_tree = input_file.Get("hist;1")

#models

gauss = Models.Gauss_pdf( 'Gauss', xvar  = ( 2.4 , 2.5 ), mean  = ( 2.45, 2.48), sigma = (0.001, 0.01 ))
poly = Models.PolyPos_pdf( 'Poly', (-100., 100.5), power = 2)

#combine models

model = Models.Fit1D(signal = gauss, background = poly)

#draw 

#pull = ****.pull_histo(input_tree)
res, frame = model.fitTo(input_tree, draw = True, nbins = 100)

h = frame.pullHist()
h.draw()


#print res
#help(Models)
