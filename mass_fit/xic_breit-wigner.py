import ostap.fitting.models as Models
import ROOT

im = ROOT.RooRealVar ('im'   , 'im'                 ,  2.42 , 2.52 )
pk = ROOT.RooRealVar ('pk'   , 'pk'                 ,  2.42 , 2.52 )

bw    = Ostap.Math.BreitWigner( pk )
sig_ap = Models.BreitWigner_pdf( 'sig_bw', breitwigner = bw, xvar = im)
bkg0 =   Models.Bkg_pdf('bkg0', xvar = im, power = 1.)

if __name__=="__main__":
    model = Models.Fit1D   ( signal = sig_ap , background = bkg0 )
    rfile = ROOT.TFile("dataset.root","READ")
    ds = rfile["da_lc"]
    ds = ds.reduce("im > 2.42 && im < 2.52")
    dh = ( ds.reduce( ROOT.RooArgSet( im ) , "im>0" ) ).binnedClone()
    r, w = model.fitTo( dh )
    r, w = model.fitTo(ds, draw=True, nbins=200)
    r.draw()
