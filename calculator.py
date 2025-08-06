print("1 - Add")
print("2- subtract")
print("3-Multiply")
print("4-divide")
option = int(input("choose an operation"))

if(option in [1,2,3,4]):
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter first number"))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        if num2 != 0:
             result = num1 //num2
        else:
            result = "Error:division by zero"
else:
    result = "Invalid operation entered"
print(f"the result of the operation is: {result}")

 
    

