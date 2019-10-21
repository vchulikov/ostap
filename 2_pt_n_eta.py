import ROOT

h = ROOT.TH1F("h", "h", 10, 0, 10)

f = ROOT.TFile.Open("test_file.root", "read")
obj = f.ds_k
obj.draw('pt:ntrk')
a = obj.y
a.draw()