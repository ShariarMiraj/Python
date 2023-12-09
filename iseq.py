# 'is' vs '==' in Python
# 'is' and '==' are both comparison operators in Python. The 'is' operator compares the identity of two objects, while the '==' operator compares the values of the objects.

a = "miraj"
b = "miraj"

print( a is b) # exact location of object in memory
print( a == b) # value

c= [1,2,3,4]
d= [1,2,3,4]

print(c is d) # exact location of object in memory  
print( c == d) # value
