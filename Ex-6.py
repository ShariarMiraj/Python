# # Library Management System in Python 


# class Book:
#   def __init__(self, book_id, title, author, quantity):
#       self.book_id = book_id
#       self.title = title
#       self.author = author
#       self.quantity = quantity

#   def display_info(self):
#       print(f"Book ID: {self.book_id}")
#       print(f"Title: {self.title}")
#       print(f"Author: {self.author}")
#       print(f"Quantity: {self.quantity}")
#       print("--------------------------")


# class Library:
#   def __init__(self):
#       self.books = {}

#   def add_book(self, book):
#       self.books[book.book_id] = book

#   def display_books(self):
#       print("Available Books:")
#       for book in self.books.values():
#           book.display_info()

#   def search_book(self, book_id):
#       return self.books.get(book_id)

#   def checkout_book(self, book_id):
#       if book_id in self.books and self.books[book_id].quantity > 0:
#           self.books[book_id].quantity -= 1
#           print("Book checked out successfully.")
#       else:
#           print("Book not available for checkout.")

#   def return_book(self, book_id):
#       if book_id in self.books:
#           self.books[book_id].quantity += 1
#           print("Book returned successfully.")
#       else:
#           print("Invalid book ID.")


# def main():
#   #  his line of code creates a new instance of the Library class and assigns it to the variable library. The Library() function is a constructor for the Library class that initializes a new library object.
 
#   library = Library()
  

#   while True:
#       print("\nLibrary Management System")
#       print("1. Add Book")
#       print("2. Display Books")
#       print("3. Search Book")
#       print("4. Checkout Book")
#       print("5. Return Book")
#       print("6. Exit")

#       choice = input("Enter your choice: ")

#       if choice == '1':
#           book_id = input("Enter Book ID: ")
#           title = input("Enter Title: ")
#           author = input("Enter Author: ")
#           quantity = int(input("Enter Quantity: "))
#           new_book = Book(book_id, title, author, quantity)
#           library.add_book(new_book)
#           print("Book added successfully.")

#       elif choice == '2':
#           library.display_books()

#       elif choice == '3':
#           book_id = input("Enter Book ID to search: ")
#           book = library.search_book(book_id)
#           if book:
#               book.display_info()
#           else:
#               print("Book not found.")

#       elif choice == '4':
#           book_id = input("Enter Book ID to checkout: ")
#           library.checkout_book(book_id)

#       elif choice == '5':
#           book_id = input("Enter Book ID to return: ")
#           library.return_book(book_id)

#       elif choice == '6':
#           print("Exiting the Library Management System. Goodbye!")
#           break

#       else:
#           print("Invalid choice. Please enter a valid option.")


# if __name__ == "__main__":
#   main()







# ////////////////////////

class Library:

  def __init__(self):
    self.noofbooks = 0
    self.books = []

  def addBook(self, book):
     self.books.append(book)
     self.noofbooks = len(self.books)

  def ShowInfo(self):
    print(f"The library has {self.noofbooks} books. The books are")

li = Library()
li.addBook("Harry Potter")
li.ShowInfo()
