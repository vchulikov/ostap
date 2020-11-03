import ROOT
import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis


def fit_gaus():
    im = ROOT.RooRealVar('im', 'im',  2.42, 2.52)
    sig_ap = Models.Gauss_pdf('Gauss', xvar  = im, mean  = (2.46, 2.47), sigma = (0.001, 0.01))
    bkg0 = Models.Bkg_pdf ('bkg0' , xvar = im, power = 1.)

    model = Models.Fit1D( signal = sig_ap, background = bkg0)

    rfile = ROOT.TFile("../datasets/test_xic_100invpb.root","READ")
    ds = rfile["da_lc"]
    ds = ds.reduce("im > 2.42 && im < 2.52")
    dh = (ds.reduce(ROOT.RooArgSet(im), "im>0")).binnedClone()

    r, w = model.fitTo(dh)
    r, w = model.fitTo(ds, draw=True, nbins=300, ncpu=4)

    pull = model.pull(ds)
    f, r, pull = model.draw(ds, nbins = 100, residual = 'P' , pull = 'P')
    return w, pull


if __name__=="__main__":
    w, h = fit_gaus()

    #DRAW IT
    canv = ROOT.TCanvas("canv", "canv", 700, 800)
    canv.Divide(1,2)
    
    canv.cd(1)
    w.Draw()
    
    canv.cd(2)
    h.Draw("HIST")

    canv.Update()
