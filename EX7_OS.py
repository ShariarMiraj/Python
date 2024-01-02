import os

files = os.listdir("Python_OS")
i = 1 
for file in files:
   if file.endswith(".png"):  #This will only show what I want to see inside the folder
      print(file)
      os.rename(f"Python_OS/{file}", f"Python_OS/{i}.png")
      i = i + 1

# os.rename(f"Python_OS/6.txt", "Python_OS/miraj.txt")