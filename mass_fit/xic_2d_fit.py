import ostap.fitting.models as Models
from   ostap.utils.timing import timing
from   ostap.histos.histos  import h1_axis
import ROOT

def fit_2d() :
    #variable inizialization
    im = ROOT.RooRealVar ('im'   , 'im'                 ,  2.42 , 2.52 )
    m23 = ROOT.RooRealVar ('m23'   , 'm23'                 ,  0.8 , 1. )
    
    #open and reduce dataset
    rfile = ROOT.TFile("dataset.root","READ")
    ds = rfile["da_lc"]
    ds = ds.reduce("im > 2.42 && im < 2.52 && m23 > 0.8 && m23 < 1.")
    dh = ( ds.reduce( ROOT.RooArgSet( im, m23 ) , "im>0" ) ).binnedClone()
    #model creation
    signal_im    = Models.Gauss_pdf( 'Gauss_x', xvar  = im, mean  = ( 2.45, 2.48), sigma = (0.001, 0.01 ))
    signal_m23   = Models.Gauss_pdf( 'Gauss_y', xvar  = m23, mean  = ( 0.8, 1.), sigma = (0.001, 0.01 ))
    bkg_poly_im  = Models.Bkg_pdf ('BkgGauss_x', xvar = im , power = 0. )
    bkg_poly_m23 = Models.Bkg_pdf ('BkgGauss_y', xvar = m23 , power = 0. )
    model_gauss = Models.Fit2D(
        signal_x = signal_im, signal_y = signal_m23, 
        bkg_1x = bkg_poly_im, bkg_1y = bkg_poly_m23)
    #model fitting
    result, frame = model_gauss . fitTo ( dh )
    result, frame = model_gauss . fitTo ( ds, draw=True)
    result.draw()

if '__main__' == __name__ :
    fit_2d()
