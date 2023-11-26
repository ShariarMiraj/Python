# for Loop with else in Python

for i in range(6):
  print(i)
  if i == 3:
    break

# after breaK THE ELSE IS NOT PRINT ANHY MORE 
else:
  print("i is smaller than 6")

print("\n")
# same this for while loop

i = 0
while i <6:
  print(i)
  i = i + 1
  if i == 3:
    break
    
else:
  print("i is smaller than 6")


#  Exmple _ 3

print(" \n")

for x in range (5):
  print("iteration no {}  in for loop".format(x+1))
else:
  print("Out of loop")
