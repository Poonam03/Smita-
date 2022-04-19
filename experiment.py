import numpy
from scipy import stats
cmarks=[0,26,32,38,70,72,78,48,66,58,42,54,70,64,60,0,20,48,50,58,42,60,42,26,32,38,65,42,54,70]
marks=[20,35,40,45,60,73,78,60,78,68,58,75,76,40,30,40,45,61,72,66,58,78,54,70,35,40,75,75,82,75]


m = numpy.mean(marks)
med = numpy.median(marks)
mod = stats.mode(marks)
x = numpy.std(marks)
t=stats.ttest_ind(cmarks,marks, axis=0, equal_var=True, nan_policy='propagate', permutations=None, random_state=None, alternative='two-sided', trim=0)

print(m,med,mod,x,t)