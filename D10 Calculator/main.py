from art import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def exit():    
    exit = input(f"Press enter to continue \nType 'new' to start over\nType 'exit' to terminate ")
    if exit.lower() == "exit":
        print("Goodbye nerd")
        cont = False
    elif exit.lower() == "new":
        calculate()
    else:
        num1 = answer

def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    for op in operations:
        print(op)
        
    cont = True
    while cont:
        symbol = input("What is the operation? ")
        num2 = float(input("What is the next number? "))
        calc = operations[symbol]
        answer = calc(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        exit = input(f"Press enter to continue \nType 'new' to start over\nType 'exit' to terminate ")
        if exit.lower() == "exit":
            print("Goodbye nerd")
            cont = False
        elif exit.lower() == "new":
            calculate()
        else:
            num1 = answer



## Seems variables assigned within functions cannot be called in a seperate function definition
# cont = True
# while cont:
#     calculate()
#     exit()
## variable ANSWER is assigned only within calculate() therefore cannot be called within exit()
## Needs to be global?

calculator()


# symbol = input("Chose another operation ")
# num3 = int(input("What is the next number? "))
# calc = operations[symbol]
# answer2 = calc(answer1, num3)
# print(f"{answer1} {symbol} {num3} = {answer2}")
