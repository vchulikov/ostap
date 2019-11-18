import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
from Functions import *

#signal
im = ROOT.RooRealVar ('im'   , 'im'                 ,  2.42 , 2.52 )
pk = ROOT.RooRealVar ('pk'   , 'pk'                 ,  2.46 , 2.47 )
gamma = ROOT.RooRealVar ('gamma'   , 'gamma'                 ,  0.001 , 0.01 )
bw    = Ostap.Math.BreitWigner( pk )
sig_ap = Models.BreitWigner_pdf( 'sig_bw', breitwigner = bw, xvar = im)

#background
bkg0  = Models.Bkg_pdf ( 'bkg0' , xvar = im , power = 0. )

if __name__=="__main__":
    model = Models.Fit1D   ( signal = sig_ap , background = bkg0 )
    rfile = ROOT.TFile("test_xic_100invpb.root","READ")
    ds = rfile["da_lc"]
    ds = ds.reduce("im > 2.42 && im < 2.52")
    dh = ( ds.reduce( ROOT.RooArgSet( im ) , "im>0" ) ).binnedClone()
    with timing():
        r, w = model.fitTo( dh )
        r, w = model.fitTo(ds, draw=True, nbins=200, ncpu=4)
    h = w.pullHist()
    draw_param( r, w, h, 200, im, 0.06*ds.sumEntries(), name="Xic", XTitle ="Mass",
                    Prefix="BW" , Type="png", var_Units = "GeV/c^{2}")
