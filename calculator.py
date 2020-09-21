#simple calculator

#adding two numbers
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y


while True:
    # promting the user to select one of the operators
    print("Choose either 1/2/3/4/5:\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Quit the calculator.")

    # prompt user to select one out of the four operators
    choice = int(input("Select 1,2,3,4,5: "))
    if choice not in (1,2,3,4,5):
        print ("You can choose from only 1,2,3,4,5")
        continue
    if choice == 5:
        print ("You are now exiting the calculator")
        break

    # Having person input number
    num1 = float(input("Enter your first number "))
    num2 = float(input("Enter your second number "))

    if choice == 1:
        print(num1, "+", num2, "=", add(num1,num2))

    elif choice == 2:
        print(num1, "-", num2,  "=", subtract(num1,num2))

    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1,num2))

    elif choice == 4:
        if num2 == 0:
            print (" Error")
        else:
            print(num1, "/", num2, "=", divide(num1,num2))


