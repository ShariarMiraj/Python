class MyClass:
  @staticmethod
  def my_static_method():
      print("This is a static method")

  @classmethod
  def my_class_method(cls):
      print("This is a class method")

  def my_instance_method(self):
      print("This is an instance method")

my_st = set([1, 2])
my_st.add(6)
my_st.update([6, 7, 8])
my_st.remove(6)
my_st.discard(7)
print(my_st)
