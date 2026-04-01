from fixpoint_pkg import fixNum
def main_menu():
    while True:
        print("\n--- Fixed-Point Calculator (Task 2) ---")
        print("1. Multiply two fixed-point numbers")
        print("2. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            #First number, enter a and b for the int and decimal part
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = int(input("  Fractional part (b): "))
            
            print("Enter second number:")
          #Same entry style as the first
            a2 = int(input("  Integral part (a): "))
            b2 = int(input("  Fractional part (b): "))
          
            #From module
            num1 = fixNum(a1, b1)
            num2 = fixNum(a2, b2)
            
            result = num1.multiply(num2)
            print(f"\nResult: {num1} * {num2} = {result}")
            
        elif choice == '2':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
#Program starts
    main_menu()
