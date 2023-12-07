# File IO in Python

# 'r' for reading   and (r) mode is defelut mode
# 'w' for writing
# 'a' for appending


# Exmple-1 ....Reading form a file..

f = open('myfl.txt', 'r')
# print(f)
txt = f.read()
print(txt)
f.close()  # if f.close it not called ..thn it will not work and print it  <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='UTF-8'>
# hello mieaj ...who are u ?..


# Exmple-2 ....Wrting form a file..

f = open('myfl.txt', 'w')
f.write('Hello, world!...')
f.close()

with open('myfl.txt', 'a') as f:
  f.write("Hey I am inside with")