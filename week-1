def power(a,b):
  if b==0:
    return 1
  elif b==1:
    return a
  else:
    if b%2==0:
      return power(a*a,b//2)
    else:
      return power(a*a,b//2)*a
    
#######################################3

liste=[4,-3,5,-2,-1,2,6,-2]
max_=0
for i in range(8):
  for j in range(i,8):
    t=0
    for k in range(i,j):
      t=t+liste[k]
    if max_<t:
      max_=t
      ibas,json=i,j
print(max_,ibas,json)
