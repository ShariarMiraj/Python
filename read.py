# # read(), readlines() and other methods | Python
# f = open('myf.txt', 'r')
# while True:
#   line = f.readline()
#   if not line:
#     # print(line, type(line))
#     break
#   print(line)


print("\n\n")
# smple !!marks calcultor for student

f = open('myf.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
    
  s1 = line.split(",")[0]
  s2 = line.split(",")[1]
  s3 = line.split(",")[2]
  print(f"Marks of student {i} in Maths is: {s1}")
  print(f"Marks of student {i} in English is: {s2}")
  print(f"Marks of student {i} in SST is: {s3}")
 
  print(line)


# EX-3
# writeline 
f = open('myf2.txt' ,'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
for line in lines:
  f.write(line + '\n')

f.close()