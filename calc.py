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

    