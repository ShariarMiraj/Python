def check_odd_even(number):
  
  try: 
      number = int(number)
      if number % 2 == 0:
          return "yes"  
      else:
          return "no" 
  except ValueError:
      return "Input is not a valid number"  


number = input("Enter a number: ")
result = check_odd_even(number)
print(result)
