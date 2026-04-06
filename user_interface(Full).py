from fixpoint_pkgFull import fixNum

def main_menu():
    while True:
        print("\n--- Fixed-Point Calculator (Task 2) ---")
        print("1. Add two fixed-point numbers")
        print("2. Subtract two-fixed point numbers")
        print("3. Multiply two fixed-point numbers")
        print("4. Divide two fixed-point numbers")
        print("5. Comparison between two fixed-point numbers")
        print("6. [BONUS]: Exponential calculation (nth power)")
        print("7. Exit")
        
        choice = input("Select an option: ")
        if choice=='1': #Calling the 'add' function
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision. This deals with a .05 and a .5 input
            p1=len(b1) #Passing this as the third argument; precision
            
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)

            result=num1.add(num2)
            print(f"{num1}+{num2}={result}")
            
        elif choice=='2': #Subtraction
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)

            result=num1.subtract(num2)
            print(f"{num1}-{num2}={result}")
        
        elif choice == '3': #Multiplication
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)
            
            result = num1.multiply(num2)
            print(f"\nResult: {num1} * {num2} = {result}")
            
        elif choice == '4': #Division
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)
            result = num1.divide(num2)
            print(f"\nResult: {num1} ÷ {num2} = {result}")
            
        elif choice == '5':
            print("Enter first number:")
            a1 = int(input("  Integral part (a): "))
            b1 = str(input("  Fractional part (b): ")) #Working with it as string to deal with precision
            p1=len(b1)
            
            
            print("Enter second number:")
            a2 = int(input("  Integral part (a): "))
            b2 = str(input("  Fractional part (b): ")) 
            p2=len(b2)

            num1=fixNum(a1,int(b1),p1)
            num2=fixNum(a2,int(b2),p2)
            result = num1.compare(num2)
            print(result)
            
        elif choice=='6':
            print("--Enter the base fixed point no:--")
            a=int(input("Integral part(a):"))
            b=str(input("Fractional part(b):"))
            p=len(b)
            base=fixNum(a,int(b),p)

            print("--Choose exponent type:--")
            print("A: Integer e.g -2,0,5")
            print("B: Fixed point no e.g 1.5")
            
            exp_option=input("Select A or B:").upper() #Ensures the user's input is always in uppercase
            result=None #Initialize
            
            if exp_option=='A': #For integers
                n=int(input("Enter the value of n:"))
                result=base.power(n)
                
            elif exp_option=='B': #For fixed point
                print("Enter exponent fixed point:")
                ae=int(input("Integral part(a):"))
                be=str(input("Fractional part(b):"))
                pe=len(be)
                exp=fixNum(ae,int(be),pe)
                result=base.power(exp)
                
            if result is not None: #Cleaning the print work
                print(f'Result:{result}')
            
        elif choice == '7':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
