import numpy
import matplotlib.pyplot as plt


fvz = 10000000

f = numpy.fromfile(open("test20"),dtype=numpy.complex64)
n = []
for i in range(0, len(f)):
  n.append(i/fvz)

plt.rcParams.update({'font.size': 22})
plt.xlabel("t[s]")
plt.ylabel("x(t)")
plt.plot(n,f)
plt.show()



