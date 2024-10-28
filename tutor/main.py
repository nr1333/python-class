def quadratic():
    # ax**2 + bx + c 

    a = input("enter 'a': ")
    b = input("enter 'b': ")
    c = input("enter 'c': ")
    x = input("enter the first'x': ")
    x2 = input("enter the second 'x': ")
    a = int(a)
    b = int(b)
    c = int(c)
    x = int(x)
    x2 = int(x2)

calculation = ax**2 + bx + c
print(calculation)

answer =
def linear_equation():
    print("Linear Equation")

    # y = mx+b
    m = input("enter 'm': ")
    x = input("enter 'x': ")
    b = input("enter 'b': ")

    m = int(m)
    x = int(x)
    b = int(b)

    y = (m*x)+b
    print(y)

    #graph the function

def polygon():
    print("Polygon")

def quadratic():
    print("Quadratic")

def math_mind():
    print("\n\n\**************** WELCOME TO MATH MIND!!! *******************")
    print("\nPlease select from one of the options below")
    print("1. Linear Equation\n2. Polygon\n3. Quadratic\n")
    option = input("Enter your option: ")
    
    option = int(option)

    match option:
        case 1:
            linear_equation()
        case 2:
            polygon()
        case 3:
            quadratic()

def print_name():
    first_name = input("Please enter you first name: ")
    last_name = input("Please enter your last name: ")
    print(first_name," ",last_name)


#********** MAIN STARTS HERE ***************
#print_name()

math_mind()
