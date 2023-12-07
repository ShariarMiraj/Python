# File IO in Python

# 'r' for reading 
# 'w' for writing
# 'a' for appending

f = open('myfile.txt', 'r')
# print(f)
txt = f.read()
print(txt)
f.close()  # if f.close it not called ..thn it will not work and print it  <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='UTF-8'>
# hello mieaj ...who are u ?..
