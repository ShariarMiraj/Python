# Dictionary Methods in Python

ep1 = { 122 : 45, 125 : 89}
ep2 = { 225 : 41, 11112 : 88}
# ep3 = { 125 : 45, 125 : 89}

ep1.update(ep2)
# ep1.pop(125)
ep1.popitem()
print(ep1)
# ep1 = update(ep1, ep3)