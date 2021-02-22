import numpy as np
import matplotlib.pyplot as plt
import math

## probability of going up exponential * probability of being in intial state wont equal probability of going down exponential * probability of being in that initial state

## why procedure for part e won't be correct: at the boundary of 5 or -5, the probability of being in the upper energy and getting to the lower energy is not equal to being in the lower energy and moving to the upper energy; harder passing criteria of the less than equal to 5 step, thus detailed balance not met. 

kT = 1.
kspring = 5.
steps = int(1e6)

xstart = 2.
xs = np.zeros(steps)
max_change_amount = 1.

x = xstart
Eold = (1/2)*kspring*x**2
accept_count = 0.0

for s in range(steps):
    drand = np.random.rand(1)
    xnew = x + max_change_amount*(drand - 0.5)*2
#    xnew = x + (x-np.cos(max_change_amount*(drand-0.5)))
    
#    xnew = x * np.exp(max_change_amount*(drand - 0.5)*2) #this doesn't work because you get a lot of very small values of xnew, resulting in passing all the time
#    print max_change_amount*(drand - 0.5)*2.
#    print xnew
    Enew = (0.5)*kspring*(xnew**2)
    r = np.random.rand(1)
    if xnew > 0.:
        if(r<math.exp(-(Enew-Eold)/kT)):
            Eold = float(Enew)
            x = float(xnew)
            accept_count = accept_count + 1

    xs[s] = x

print("Accepted fraction = %g" % (accept_count/steps))

plt.subplot(1,2,1)
plt.plot(xs[0:499])
plt.ylabel("x")
plt.xlabel("Monte Carlo steps")

plt.subplot(1,2,2)
xf = np.linspace(-np.max(abs(xs)),np.max(abs(xs)),1000)
std_x = math.sqrt(kT/kspring)
pt = (2*1/math.sqrt(2*math.pi*std_x**2))*np.exp(-(xf**2)/(2*std_x**2))
plt.hist(xs,bins=100,density=True)
plt.plot(xf,pt)
plt.yscale("log")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()
