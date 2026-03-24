tables = {i: None for i in range(1, 21)} 
def display_available_tables():
    print("\nAvailable Tables:")
    available = [table for table, name in tables.items() if name is None]
    if available:
        print(available)
    else:
        print("No tables available.")
def reserve_table():
    name = input("\nEnter customer name: ")
    table_no = int(input("Enter table number to reserve (1-20): "))
    if table_no < 1 or table_no > 20:
        print("Invalid table number!")
    elif tables[table_no] is not None:
        print(f"Table {table_no} is already reserved by {tables[table_no]}.")
    else:
        tables[table_no] = name
        print(f"Table {table_no} successfully reserved for {name}.")
def show_all_reservations():
    print("\n--- Table Reservations ---")
    for table, name in tables.items():
        if name:
            print(f"Table {table}: Reserved by {name}")
        else:
            print(f"Table {table}: Available")
while True:
    print("\n--- Restaurant Reservation System ---")
    print("1. Display Available Tables")
    print("2. Reserve Table")
    print("3. Show All Reservations")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        display_available_tables()
    elif choice == '2':
        reserve_table()
    elif choice == '3':
        show_all_reservations()
    elif choice == '4':
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Please try again.")
