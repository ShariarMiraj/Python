# break and continue in Python 

for i in range(12):
  print("5 X", i ,"=", 5 * i)
  if( i == 10 ):
    break
    
print("Loop ended")



print("\n\n")
print("This is Iteration :")

for i in range(12):
  if( i == 10 ):
    print("Skip the iteration")
    continue

  print("5 X", i ,"=", 5 * i)



print("\n\n")
print("This is do while emulated: ")

i = 0 
while True:
  print(i)
  i += 1
  if( i == 10 ):
    break

print("\n\n Example Number 2 Emulation  :")
print("\n\n")


while True:
  print("Enter a number : ")
  num = input()
  if( num == "exit" ):
    break
  print("You entered : ", num)
  
print("Loop ended")
  

    

