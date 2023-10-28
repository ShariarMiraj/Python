# Loops
# for loop
for i in range(1, 5):
    print(i)

print("\n\n\n")
# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

print("\n\n\n")
# break and continue
for i in range(1, 5
               ):
  if i == 3:
    break
  print(i)

print("\n\n\n")
for i in range(1, 5
               ):
  if i == 3:
    continue
  print(i)

print("\n\n\n")
# nested loops
for i in range(1, 5
               ):
  for j in range(1, 5
                 ):
    print(i, j)
    
print("\n\n\n")
# break and continue in nested loops
for i in range(1, 5
               ):
  for j in range(1, 5
                 ):
    if i == 3:
      break
    print(i, j)
    
print("\n\n\n")
for i in range(1, 5
               ):
  for j in range(1, 5
                 ):
    if i == 3:
      continue
    print(i, j)
    
