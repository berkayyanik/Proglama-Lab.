List_1=[0,5,25,100,5,5,0,100]

def my_h(List_1):
  my_d=dict()  # {}
  for i in List_1:
    if i in my_d:
      my_d[i] = my_d[i] + 1
    else:
      my_d[i] = 1
  return my_d
print(my_h(List_1))

#############################

def my_h2(List_1):
  my_d2=dict()  # {}
  for i in List_1:
    if i not in my_d2:
      my_d2[i] = 1
    else:
      my_d2[i] += 1
  return my_d2
print(my_h2(List_1))

##############################
known = {0:0,1:1}

def fibo_rec(n):
  if n in known:
    return known[n]
  else:
    result = fibo_rec(n-1) + fibo_rec(n-2)
    known[n] = result
    return result

#############################

from sympy import Finiteset

def probability(space,event):
    return len(event)/len(space)

def check_prime(number):
    if number!=1:
        for i in range(2,number):
            if number%i==0:
                return False
    else:
        return False
    return True

space =Finiteset(*range(1,21))
primes =[]
for num in space:
    if check_prime(num):
        primes.append(num)
event=Finiteset(*primes)
p=probability(space,event)
print(p)
