# Prompt user to input names and grades of students
# Create empty dictionary to store values

books = {
    "The Great Gatsby": "available",
    "To Kill a Mockingbird": "checked out",
    "1984": "available",
}

ADD_BOOK = 1
CHECK_OUT = 2
RETURN = 3
VIEW = 4
QUIT = 5

# Display options for user
# Initialize no answer
user_choice = ""
while user_choice != 5:
    try:
        user_choice = int(input("What would you like to do? \n" +
      "1. Add book \n" +
      "2. Check out a book \n" +
      "3. Return a book \n" +
      "4. View all books \n" +
      "5. Quit \n"))
        break # Exit loop if input is invalid
    except ValueError or TypeError:
        user_choice = int(input("Invalid input. Please enter options 1 - 5: "))

    if user_choice == ADD_BOOK:
        add_book = input("Enter book title: ")
        if add_book in books:
            print("Book already exists. \n")
        else:
            # Assign key value (book name) with the default value 'available' 
            books[add_book] = 'available' # It will automatically add to the books dictionary 
            print(f"{add_book} has been added to the library as 'available'. \n ")
    elif user_choice == CHECK_OUT:
        check_out = input("Enter the title of the book to check out: ")
        if check_out in books: # Check if the book is in the dictionary / exists
            if books[check_out] == 'available': # Check if user input book's value is available
                books[check_out] = 'checked out' # Change value to checked out
                print(f"You have successfully checked out '{check_out}'. ")
            else:
                print("Sorry. The book is not available. ")
    elif user_choice == RETURN: 
        return_book = input("Enter the title of the book you would like to return: ") 
        if return_book in books: # Check if the book exists
            if books[return_book] == 'checked out': # Check if the value of the book is 'checked out'
                books[return_book] = 'available'
                print(f"You have successfully returned {return_book}")
            else:
                print("Sorry. Book does not belong at this library location. ")
    elif user_choice == VIEW:
        print(books)
    elif user_choice == QUIT:
        print("Thank you - Come again! ")