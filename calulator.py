division_symbol = '\u00F7'

num1 = input("Enter a number: ")
operator = input("Enter an operation (add: +, subtract: -, multiply: * or divide: /): ")
num2 = input("Enter a number: ")

def equals(operator):
    match operator:
        case "+":
            result = int(num1) + int(num2)
            print(f"{num1} + {num2} = {result}")
        case "-":
            result = int(num1) - int(num2)
            print(f"{num1} - {num2} = {result}")
        case "*":
            result = int(num1) * int(num2)
            print(f"{num1} x {num2} = {result}")
        case "/":
            result = int(num1) / int(num2)
            print(f"{num1} {division_symbol} {num2} = {result}")
            
equals(operator)