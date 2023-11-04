# Functions in Python

def calculationGmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)
  
a = 6
b = 2
if(a>b):
  print("First Number is Greater number ")
else:
  print("Second Number is Greater number ")
calculationGmean(a,b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)

print("\n")

c=12
d=2
if(c>d):
  print("First Number is Greater number ")
else:
  print("Second Number is Greater number ")
calculationGmean(c,d)
# gmean2 = (a+b)/(a-b)
# print(gmean2)


print("\n")
# Other way less And Greater
def calculationGmean1(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
  if(a>b):
    print("First Number is Greater number ")
  else:
    print("Second Number is Greater number ")

def isLesser(a, b):
  pass
  #        (pass means -> I work lttr in this functions)

a = 8 
b= 6
isGreater(a,b)
calculationGmean1(a,b)

c=12
d=14
isGreater(c,d)
calculationGmean1(c,d)