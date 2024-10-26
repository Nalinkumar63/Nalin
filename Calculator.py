print("1 - Sum")
print("2 - Subtract")
print("3 - Product")
print("4 - Divide")
option = int(input("choose an operation: "))

if(option in[1, 2,3,4]):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num // num2
    
else:
    print("Invalid operation entered")
    
print("The result of the operation is {}".format(result))
