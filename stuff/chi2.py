import ROOT
from   ostap.histos import compare

def ostap_chi2():
    #Load TRandom3 module
    R = ROOT.TRandom3()
    R.SetSeed(0)
    #Set bins number
    bins = 50
    #Create & fill & draw histograms
    hist1 = ROOT.TH1F("h1", "", bins, 0., 5)
    hist2 = ROOT.TH1F("h2", "", bins, 0., 5)
    for i in range(bins):
        hist1.SetBinContent(i, R.Integer(15))
        hist2.SetBinContent(i, R.Integer(15))

    chi2ndf, prob  = hist1.chi2_cmp ( hist2 )
    print('chi2/ndf = {0}'.format(chi2ndf))
    
    return 0


if "__main__" == __name__ :
    ostap_chi2()







