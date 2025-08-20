#Defining each function(Add, Sub, Mult, Div, Exp, along with input validation).

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return 'Error: Cannot divide by 0.'
    return a / b
def exp(a, b):
    return a ** b

#Defined calculator function, created loop.
def calculator():

    print('Welcome to the CLI Python Calculator')

#Allows user to choose which previously declared option they would like the calculator to perform.
    while True: 
        print ('Choose an operation')
        print('1) Addition')
        print('2) Subtraction')
        print('3) Multiplication')
        print('4) Division')
        print('5) Exponent ^')
        print('6) Exit')

        choice = input('Enter operation number: ')

        #Lets user exit.
        if choice == '6':
            print('Goodbye, thanks for using the CLI Python Calculator!')
            break
        #Handles error in user input, loops again.
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please select 1-6.")
            continue
        #Accepts user's numbers and puts them in variables.
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))   
        #More error handling, specifically for invalid input type.
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue 
        #Implementing operations.
        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        elif choice == "5":
            result = exp(a, b)
        
    #Display of result.
        print(f'Result: {result}')

# Run the calculator, but only if this file is being executed directly.
if __name__ == "__main__":
    calculator()