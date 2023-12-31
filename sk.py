# seek(), tell() and other functions
# are used to work with file objects and their positions within a file.

with open('file.txt' , 'r') as f:
  print(type(f))
  # Move to the 10th byte in the file
  f.seek(10)
  # Read the next 5 bytes
  print(f.tell())
  data = f.read(5)
  print(data)

# tell() function returns the current position within the file, in bytes.

# truncate()

with open('smile.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

# for check or print  wittn option
with open( 'smile.txt', 'r') as f:
  print(f.read())