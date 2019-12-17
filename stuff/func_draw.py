import ostap.fitting.models as md
import ROOT

def draw_gaussian():
 im    = ROOT.RooRealVar('im', 'im', 0., 1.)
 model_gauss = md.Gauss_pdf('Gauss', im, mean = 0.5, sigma = 0.01)
 model_gauss.draw_options['total_fit_options'] = ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.LineWidth(5)
 model_gauss.draw()

def draw_jsu():
 im    = ROOT.RooRealVar('im', 'im', 0., 1.)
 model_jsu = md.JohnsonSU_pdf( 'J_SU', im, xi = 0.5, lambd = .1, delta = 5., gamma = 0.5)
 model_jsu.draw_options['total_fit_options'] = ROOT.RooFit.LineColor(ROOT.kBlue), ROOT.RooFit.LineWidth(5)
 model_jsu.draw()
 
def draw_apol2():
 im    = ROOT.RooRealVar('im', 'im', 0., 1.)
 model_apol2 = md.Apolonios2_pdf( 'Apol2', im, mean = 0.5, sigma = .05, asymmetry = 0., beta = 1.)
 model_apol2.draw_options['total_fit_options'] = ROOT.RooFit.LineColor(ROOT.kGreen), ROOT.RooFit.LineWidth(5)
 model_apol2.draw()

def draw_cb():
 im    = ROOT.RooRealVar('im', 'im', 0., 1.)
 model_cb = md.CrystalBall_pdf( 'CB', im, mean = 0.5, sigma = 0.1, alpha = 5., n = 1.0)
 model_cb.draw_options['total_fit_options'] = ROOT.RooFit.LineColor(ROOT.kMagenta), ROOT.RooFit.LineWidth(5)
 model_cb.draw()

if __name__=="__main__":
 draw_gaussian()
 draw_jsu()
 draw_apol2()
 draw_cb()
