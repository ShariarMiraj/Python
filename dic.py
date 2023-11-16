# Dictionaries are ordered collections of key-value pairs.
# Dictionaries are mutable.
# Dictionaries are iterable.
# Dictionaries are indexed by keys.
# Dictionaries are indexed by keys.

dic = {
  334:"Miraj",
  "B": "Shahriar",
  "C": "AMMU",  
}

print(dic[334])
print(dic["B"])
print(dic["C"])

info = {
  "Name": "Miraj",
  "Age": 22,
  "Gender": "Male",
  "Occupation": "Student",
  "City": "Pune",
  "State": "Maharashtra",
  "Country": "India",
  "Phone": "9876543210",
  "Email": "xcvkp@example.com",
  "Address": "Pune, Maharashtra, India",
  "DOB": "18 July 2001",
  "Height": "5', 7",
  "Weight": "60 kg",
  "Marital Status": "Single",
  "Languages": "English, Hindi, Urdu",
  "Hobbies": "Reading, Writing, Travelling",
  "Interests": "Music, Movies, Travelling",
  "Favorite Food": "Pizza, Burger, Pasta",
  "Favorite Color": "Blue, Red, Green",
  "Favorite Subject": "Maths, Science, Social Science",
  "Favorite Book": "Harry Potter, Lion King, Diary of a Wimpy Kid",
  "Favorite Movie": "The Matrix, Harry Potter, Diary of a Wimpy Kid",
  "Favorite Quote": "The Matrix, Harry Potter, Diary of a Wimpy Kid",
  "Favorite Song": "The Matrix, Harry Potter, Diary of a Wimpy Kid",
  "Favorite Band": "The Matrix, Harry Potter, Diary of a Wimpy Kid",
  "Favorite Actor": "The Matrix, Harry Potter, Diary of a Wimpy Kid",

  }
print(info)

print(" ")

# Accessing single value
info = {"Name": "Miraj", "Age": 22, 'eligible':True}
# print(info["Name"])
# print(info["Age"])
# print(info["eligible"])
print(info["Name"], info["Age"], info["eligible"])
print(info.get("Name"))
print(info.get("Name2"))   # if i want show this error msg or say like unfind value showing .
print(info.get("Name2", "Not Found"))

