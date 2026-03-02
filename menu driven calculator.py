#Menu driven calculator
def add(a,b):
        sum = a + b
        print(a, "+" , b,"=" , sum)

def substract(a,b):
        difference = a - b
        print(a, "-", b, "=" , difference)

def multiply(a,b):
        product = a * b
        print(a, "*", b, "=", product)

def devide(a,b):
        devision = a / b
        print(a, "/", b, "=", devision)
        print("Welcome to menu driven calculator")
while True:
     print("\nMENU")  
     print("1. addtion")
     print("2. substraction")
     print("3. multiplication")
     print("4. division")
     print("5. exit")
     choice = int(input("\n Enter the choice = "))
     if choice == 1:
        print("\n addition \n")
        a = int(input("Enter the a = "))
        b = int(input("Enter the b = "))
        add(a,b)
        
     elif choice == 2:
        print("\n substraction\n")
        a = int(input("Enter the number a = "))
        b = int(input("Enter the number b = "))
        substract(a,b)
     elif choice == 3:
        print("\n multiplication\n")
        a = int(input("Enter the number a = "))
        b = int(input("Enter the number b = "))
        multiply(a,b)
     elif choice == 4:
        print("\n Division\n")
        a = int(input("Enter the number a = "))
        b = int(input("Enetr the number b = "))
        devide(a,b)
     elif choice == 5:
        break
     else:
        print("plese provide the valid input")