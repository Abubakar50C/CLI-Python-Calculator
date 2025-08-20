#Defining each function(Add, Sub, Mult, Div, Exp, along with input validation)

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

    while True:
        print ('Choose an operation')
        print('1) Addition')
        print('2) Subtraction')
        print('3) Multiplication')
        print('4) Division')
        print('5) Exponent ^')
        print('6) Exit')

        choice = input('Enter operation number: ')

        if choice == '6':
            print('Goodbye, thanks for using the CLI Python Calculator!')
            break
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please select 1-6.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))   
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue 


    