import math
from pylab import *
xt = [2]
t = [0]
k = 1

dt = 0.0001
Vx = 0
for i in range(800000):
    t.append(dt*i)
    a = -k*xt[i]
    xt.append(xt[i] + dt*Vx)
    Vx = Vx + dt*a
plot(t,xt)
show()