# Decorators in Python 

def greet(fx):
  
  def mfx():
    print("this side  from miraj...")
    fx()
    print("thanks for using this function")
  return mfx


@greet
def miraj():
  print("Helllo from miraj..")

miraj()


# EXMPLE _3  from https://www.geeksforgeeks.org/decorators-in-python/

# time of a function using a decorator.
import time 
import math 

def calculate_time(fu):

  def inner(*args , **kwargs):

    begin = time.time()
    fu(*args , **kwargs)
    end = time.time()
    print(f"Time taken by {fu.__name__} is {end - begin}")
  return inner
  
@calculate_time
def factorial(n):
  time.sleep(2)
  print(math.factorial(n))

factorial(10)

