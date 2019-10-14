from ROOT import TFile, TH1F

#open db - file
dbname = 'data.ds'
f = open(dbname, 'r')

#create root - file
tree = TFile('data.root','RECREATE')

#create hist
h1f = TH1F( 'hist', 'hist', 1000, 2.43, 2.5 )

#fill hist
for i in f:
 h1f.Fill(float(i))

#write hist in file
h1f.Write()

#close files
tree.Close()
f.close()
