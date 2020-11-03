import ROOT
import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
from ostap.core.core import cpp

def fit_jsu():
    im   = ROOT.RooRealVar ('im' , 'im' ,  2.42 , 2.52)
    pk   = ROOT.RooRealVar ('pk' , 'peak' , 2.47 , 2.46, 2.48)
    gam  = ROOT.RooRealVar ('gamma' , 'gamma' , 1. , 0., 1.5)
    delt = ROOT.RooRealVar ('delta' , 'delta' , 0. , 0., 20.0)

    sig_ap = Models.JohnsonSU_pdf('sig_ap', xvar=im, xi = pk, lambd = None, \
                                            delta = delt, gamma=gam)
    bkg0   = Models.Bkg_pdf ('bkg0', xvar = im, power = 1.)

    model = Models.Fit1D(signal = sig_ap, background = bkg0)
    rfile = ROOT.TFile("../datasets/test_xic_100invpb.root","READ")
    ds = rfile["da_lc"]
    ds = ds.reduce("im > 2.42 && im < 2.52")
    dh = (ds.reduce(ROOT.RooArgSet(im), "im>0")).binnedClone()

    with timing():
        r, w = model.fitTo(dh)
        r, w = model.fitTo(ds, draw=True, nbins=200, ncpu=4)
    r.draw()


def fit_bw():
    im = ROOT.RooRealVar ('im', 'im',  2.42, 2.52 )
    pk = ROOT.RooRealVar ('pk', 'pk',  2.47, 2.46, 2.48 )
    bw = cpp.Ostap.Math.BreitWigner(pk)
    sig_ap = Models.BreitWigner_pdf('sig_bw', breitwigner = bw, xvar = im)
    bkg0 =   Models.Bkg_pdf('bkg0', xvar = im, power = 2.)

    model = Models.Fit1D   ( signal = sig_ap , background = bkg0 )
    rfile = ROOT.TFile("../datasets/test_xic_100invpb.root","READ")
    ds = rfile["da_lc"]
    ds = ds.reduce("im > 2.42 && im < 2.52")
    dh = (ds.reduce(ROOT.RooArgSet(im), "im>0")).binnedClone()

    with timing():
        r, w = model.fitTo(dh)
        r, w = model.fitTo(ds, draw=True, nbins=200)
    r.draw()


if __name__=="__main__":
    fit_jsu()
    fit_bw()


