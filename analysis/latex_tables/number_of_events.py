# table with Lc(Yc) - events ---> | (eta_i, eta_f) | (pt_i, pt_f) | N_ev_lc_val +- N_ev_lc_err | N_ev_scpp_val +- N_ev_scpp_err | 
import ROOT, numpy

if __name__ == "__main__" :
 data = numpy.genfromtxt('data_nominal.csv', delimiter = ',')
 length_x = numpy.size(data, 0)

 for i in range(length_x - 1):
  print("(" + str(data[i + 1, 1]) +" ; " + str(data[i + 1, 2]) + ") & (" + str(data[i + 1, 3]) +" ; " + str(data[i + 1, 4]) + ") & " + str(int(round(data[i + 1, 5]))) + "~$\pm$  "+ str(int(round(data[i +1, 6]))) + " & " + str(int(round(data[i + 1, 7]))) + "~$\pm$  "+ str(int(round(data[i +1, 8]))) + " & " +"value" + str(i)  +"\\" + "\\")
