import numpy
marks=[0,26,32,38,70,72,78,48,66,58,42,54,70,64,60,0,20,48,50,58,42,60,42,26,32,38,65,42,54,70]

m = numpy.mean(marks)
med = numpy.median(marks)
mod = numpy.mode(marks)
x = numpy.std(marks)

print(m,med,mod,x)