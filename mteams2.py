from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
p = x*(x+x)

p = (x+2)*(x+3)

from sympy import factor

expr = x**2 - y**2
factors = factor(expr)
expand = expand(factors)

from sympy import pprint
pprint(factors)

x = Symbol('x')
series = x
n = 5
for i in range(2,n+1):
  series = series + (x**i)/i
pprint(series)

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1 , y:2})
res

r = expr.subs({x:1-y})
r

x = Symbol('x')
series = x
n = 5
x_value = 10
for i in range(2,n+1):
  series = series + (x**i)/i
pprint(series)
series_value = series_subs({x:x_value})
series_value
