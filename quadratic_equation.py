# Author name : Kote Seema M ('https://github.com/seema-kote/')
# Created Date : 12th Sep 2017

import cmath
a=2
b=3
c=4
d = (b**2)-(4*a*c)
print type(d)
ansPos = (-b+cmath.sqrt(d))/2*a
ansNeg = (-b-cmath.sqrt(d))/2*a
print "Solution:{0},{1}".format(ansPos,ansNeg)
