import ROOT
import ostap.io.rootshelve as rs

def print_data():
    db_file = rs.open("../datasets/test_xic_100invpb.root", 'r')
    ds = db_file["da_lc"]
    im   = ROOT.RooRealVar ('im', 'im'  , 2.43, 2.51)
    dh = (ds.reduce(ROOT.RooArgSet(im) , "im>0")).binnedClone()

    #Get full info about 11th event
    ds.get(11).Print("V")
    #Get mass info about 11th event
    print(ds.get(11).getRealValue("im"))
    
if "__main__" == __name__ :
    print_data()
