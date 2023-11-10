# Manipulating; tuples:

continues = ("Bangladesh", "India", "China", "Pakistan", "Nepal")
temp = list(continues)
temp.append("Bhutan")  # add items
temp.pop(3)  # remove items
temp[2] = "Finland"  # replace items or change
continues = tuple(temp)
print(continues)

# EX ;2

continues = ("Bangladesh", "India", "China", "Pakistan", "Nepal")
continues2 = ("Canada", "USA", "Mexico")
southaisa = continues + continues2
print(southaisa)

print("\n\n")
# EX ; 3 .. how come the numbr

tuple1 = (1, 2, 3, 4, 5, 5)
res = tuple1.count(5)
res1 = tuple1.index(3)
res2 = len(tuple1)
print("Couting 5 : ", res , "\nIndex of 3 : ", res1 , "\nLength of tuple : ", res2)
