import ROOT
import ostap.fitting.models as Models
from ostap.core.core import cpp

#variables
imc = ROOT.RooRealVar('imc', 'imc', 1., 3.)
pk = ROOT.RooRealVar('pk' , 'peak', 0.)

#signal
bw = cpp.Ostap.Math.BreitWigner(pk)
sig_bw = Models.BreitWigner_pdf('sig_bw', breitwigner = bw, xvar = imc)
sig_bw.gamma.setVal(0.20)
sig_bw.gamma.setError(0.01)
sig_bw.mean.setVal(2.10)
sig_bw.mean.setError(0.10)

#background
bkg0 = Models.PolyPos_pdf('bkg', imc , power = 1 )
bkg0.phis[0].setVal(2.72)
bkg0.phis[0].setError(0.02)

#compound model
model = Models.Fit1D(signal = sig_bw, background = bkg0)
model.draw()
