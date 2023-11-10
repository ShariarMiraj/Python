# Manipulating; tuples:

continues = ("Bangladesh","India","China","Pakistan","Nepal")
temp = list(continues)
temp.append("Bhutan")    # add items
temp.pop(3)              # remove items
temp[2] = "Finland"      # replace items or change 
continues = tuple(temp)
print(continues)
