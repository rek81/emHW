import math
import numpy as np
import matplotlib.pyplot as plt

#force for one charge: F = (-q1**2*r1*d)/(d**2-r1**2)**2 + (q1**2*r1)/(d**3) + (q1*q2)/(d**2)
#Each force should be subtracted from the center~ should get convergence within 10 steps

def ImageCharges(r1, r2, q1, q2, d, steps):
    
    #is = image charge of sphere
    #io = image charge of other sphere

    xs = np.zeros(steps)

    q1startis = q1 * (-r2/d)
    d1startis = (d) - (r2**2/d)
    q2startis = q2 * (-r1/d)
    d2startis = 0. + (r1**2/d)

    q1is = q1startis
    d1is = d1startis
    q2is = q2startis
    d2is = d2startis
    
 
    Qc1 = q1
    Qc2 = q2
    
    F = (q1*q2)/d**2 

    for i in range(steps):
        q1startio = q1startis * (-r1/(d-d1startis))
        d1startio = 0. + (d1startis) # image charge of image charge of Q1 located at origin of 2st sphere - unit distance away 
        q2startio = q2startis * (-r2/d2startis)
        d2startio = (d) - (r2**2/(d-d2startis)) # image charge of image charge of Q2 located at origin of 2nd sphere - unit distance away 
        q1io = q1startio
        d1io = d1startio
        q2io = q2startio
        d2io = d2startio


        q1is = q1io
        q2is = q2io
        d1is = d1io
        d2is = d2io
       
#        q1newis = q1is
#        d1newis = d1is
#        q2newis = q2is
#        d2newis = d2is



        q1newio = q1io
        d1newio = d1io
        q2newio = q2io
        d2newio = d2io

        Qc1 += -q2is-q1io
        Qc2 += -q1is-q2io

        F = -(q1io**2*r1*d)/(d**2-r1**2)**2 - (q2io**2*r1*d)/(d**2-r2**2)**2 + (Qc1**2*r1)/d**3 + (Qc2**2*r2)/d**3 +  q1*q2/d**2
#        F = -(Qc1**2*r1*d)/(d**2-r1**2)**2 -(Qc2**2*r2*d)/(d**2-r2**2)**2 + (Qc1**2*r1)/d**3 + (Qc2**2*r2)/d**3 +  q1*q2/d**2
#        F = Qc1/d + Qc2/d + q1is/d1is + q2is/d2is + q1io/d1io + q2io/d2io

#        F += (q1is*q1)/d1is**2 + (q2is*q1)/d2is**2 + (q1io*q1)/d1io**2 + (q2io*q1)/q2io**2 + (Qc2*q1)/d**2 # set k = 1
#        F += (Qc1*Qc2)/d**2 + (q1is*q1)/(d1is-d)**2 + (q2is*q1)/(d2is-d)**2 + (q1io*q1)/(d1io-d)**2 + (q2io*q1)/(q2io-d)**2  



    
        xs[i] = F

    return xs

s = 15
xaxis = []
for i in range(s):
    xaxis.append(i)

test1 = ImageCharges(1., 1., 1., 1., 2.5, s)
#test2 = ImageCharges(1., -2., 1., 2., 3.5, s)
print test1
print xaxis
plt.plot(xaxis, test1)
plt.show()
