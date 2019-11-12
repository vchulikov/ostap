import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
from Functions import *


im = ROOT.RooRealVar ('im'   , 'im'                 ,  2.42 , 2.52 )
pk = ROOT.RooRealVar ('pk'   , 'peak   '   , 2.2875 ,  2.46 , 2.248 )
gam = ROOT.RooRealVar ('gamma'   , 'gamma'     , 1. ,  0. , 1.5 )
delt = ROOT.RooRealVar ('delta'   , 'delta' , 0.0000 , 0.000 , 20.000 )


sig_ap = Models.JohnsonSU_pdf( 'sig_ap', xvar=im, xi = None, lambd = None, delta = delt, gamma=gam)
bkg0  = Models.Bkg_pdf ( 'bkg0' , xvar = im , power = 1. )


if __name__=="__main__":
    model = Models.Fit1D   ( signal = sig_ap , background = bkg0 )
    rfile = ROOT.TFile("test_xic_100invpb.root","READ")
    ds = rfile["da_lc"]
    ds = ds.reduce("im > 2.42 && im < 2.52")
    dh = ( ds.reduce( ROOT.RooArgSet( im ) , "im>0" ) ).binnedClone()
    with timing():
        r, w = model.fitTo( dh )
        r, w = model.fitTo(ds, draw=True, nbins=100, ncpu=4)
    h = w.pullHist()
    draw_param( r, w, h, 100, im, 0.06*ds.sumEntries(), name="Lc", XTitle ="Mass",
                    Prefix="Johnson_SU" , Type="png", var_Units = "GeV/c^{2}")
