# Defult fanction

def avarege(a =5,b=2):
  print("The avarege of ", a, " and ", b, " is : ", (a+b)/2)

avarege(5,2)
avarege(b=5,a=2)
avarege(a=5,b=2)
avarege(a=5,b=5)
avarege()


print("\n")
# variable length argumrnt

def avarege1(*args):
  sum = 0
  for i in args:
    sum = sum + i
  print("The avarege of ", args, " is : ", sum/len(args))

avarege1(5,2,6,7,8,9)
avarege1(1,2,3,4,5,6,7,8,9)
# avarege1(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

print("\n")
# keyword argumrnt
def avarege2(**kwargs):
  sum = 0
  for i in kwargs:
    sum = sum + kwargs[i]
  print("The avarege of ", kwargs, " is : ", sum/len(kwargs))

avarege2(a=5,b=6,c=7,d=8,e=9)
avarege2(a=5,b=6,c=7,d=8,e=9,f=10,g=11,h=12,i=13,j=14,k=15,l=16,m=17,n=18,o=19,p=20,q=21)









  