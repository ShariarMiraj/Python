name = "Python"
print("helo", name)
# Output: helo Python
print("\n")

# 3 cot and single cot
anotherfriend = '''Hi I am .Net
hi c++
hi java
"hi sql"
hi python'''
print(anotherfriend)
# Output: Hi I am .Net
# hi c++
# hi java
# hi python

#////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\//////

# Indexing ( python is like a arry of characater)

naam = "Python"
print(naam[0])
print(naam[1])  # Output: P y

# slicing ( slice the string)
print(naam[0:2])
# Output: Py
name = "miraj , singh"
print(name[0:3])

#////////////////////////////////////////////////
# Lenght of string
print(len(name))
# Output: 13

fruit = "Python"
len1 = len(fruit)
print("python is ", len1, "word")
# Output: 6

#////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\

#String arry and Slicing

fruit = "Mango"
len1 = len(fruit)
print(len1)
print(fruit[0:3])

nm = "MIRAJ"
print(nm[-4:-2])

#////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\

# String are immutable

a = "Miraj"
print(len(a))
print(a)

str1 = "AcBHHiimm"
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.swapcase())

# rstrip
str2 = "!!!Miraj !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print(str2.rstrip("!"))

# replace
str3 = "Miraj "
print(str3.replace("Miraj", "Singh"))

# split
str4 = "Miraj , Madmud  , singh"
print(str4.split(","))

# join
str5 = "Miraj , Madmud  , singh"
print(str5.join(" +"))

# startswith
str6 = "Miraj , Madmud  , singh"
print(str6.startswith("Miraj"))

# endswith
str7 = "Miraj , Madmud  , singh"
print(str7.endswith("singh"))

# capitilize
str8 = "miraj  Shahriar MAHMUD "
print(str8.capitalize())

# strip
str9 = "Miraj , Madmud  , singh"
print(str9.strip())

# zfill
str10 = "5"
print(str10.zfill(5))

# center
str11 = "  Miraj  Madmud  "
print(str11.center(20))

# rjust
str12 = "  Miraj  Madmud  "
print(str12.rjust(50))

# count
str13 = "Miraj , Madmud  , singh"
print(str13.count("i"))




