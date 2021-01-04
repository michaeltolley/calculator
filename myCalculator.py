print("this is my calculator.")
operation = input("chooes an arithmetic operation (add, subtract, multiply, divide): ")


firstNumber = int(input("Enter the first number here:  "))
secondNumber = int(input("Enter the second number here:  "))

if operation == "add":
    sum = firstNumber + secondNumber
    answer = sum

if operation == "difference":
    difference =  firstNumber - secondNumber
    answer = difference

if operation == "multiply":
    product = firstNumber * secondNumber
    answer = product

if operation == "divide":
    quotient = firstNumber / secondNumber
    answer = quotient

print("this is your answer  " + str(answer) )