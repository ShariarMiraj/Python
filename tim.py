# Time Module in Python

import time

current_time = time.time()
print(current_time)



print(4)
time.sleep(3)
print("This is printed after 3 seconds")




current_time = time.time()
formatted_time = time.ctime(current_time)
print(formatted_time)



current_time = time.time()
local_time = time.localtime(current_time)
print(local_time)

print("\n")
current_time = time.time()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time))
print(formatted_time)



current_time = time.time()
utc_time = time.gmtime(current_time)
print(utc_time)