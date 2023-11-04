# break and continue in Python 

for i in range(12):
  print("5 X", i ,"=", 5 * i)
  if( i == 10 ):
    break
    
print("Loop ended")

print("\n\n")

for i in range(12):
  if( i == 10 ):
    print("Skip the iteration")
    continue

  print("5 X", i ,"=", 5 * i)


    

