# Regular Expressions in Python

import  re

# pattern = "cse"
pattern = r"[A-Z]+yclone" 
text = " this is shahriar mahmud miraj. he read in aiub , he completed cse and Cyclone ,  Dyclone "

# match = re.search(pattern, text)
# print(match)


matches = re.finditer(pattern, text)
for match in matches:
  print(match)