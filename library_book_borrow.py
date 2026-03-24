library = {} 
def borrow_book():
    book = input("\nEnter book name: ").lower()
    name = input("Enter borrower name: ")
    if book in library:
        print(f"'{book}' is already borrowed by {library[book]}")
    else:
        library[book] = name
        print(f"'{book}' borrowed successfully by {name}")
def return_book():
    book = input("\nEnter book name to return: ").lower()
    if book in library:
        del library[book]
        print(f"'{book}' returned successfully")
    else:
        print("Book was not borrowed")
def display_borrowed():
    print("\n--- Borrowed Books ---")
    if not library:
        print("No books borrowed")
    else:
        for book, borrower in library.items():
            print(f"{book} → {borrower}")
def check_availability():
    book = input("\nEnter book name: ").lower()
    if book in library:
        print(f"Not available (borrowed by {library[book]})")
    else:
        print("Available")
while True:
    print("\n--- Library System ---")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Display Borrowed Books")
    print("4. Check Book Availability")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        borrow_book()
    elif choice == '2':
        return_book()
    elif choice == '3':
        display_borrowed()
    elif choice == '4':
        check_availability()
    elif choice == '5':
        print("Exiting system...")
        break
    else:
        print("Invalid choice!")
