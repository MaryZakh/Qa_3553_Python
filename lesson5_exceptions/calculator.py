#LOW LEVEL - It only performs calculations. It doesn`t interact with the user
def calculate(a:float, b:float,op:str):
    if op == '+':
        return a+b
    elif op =='-':
        return a-b
    elif op =='*':
        return a*b
    elif op =='/':
        return a/b #ZeroDivisionError if b==0
    else:
        raise ValueError(f"Unknown action: {op}")

#MIDDLE LEVEL - parsing. Convert string into numbers
def pars_and_calc(a_str: str, b_str:str,op:str):
    a = float(a_str) #ValueError if not a number
    b = float(b_str) #ValueError if not a number
    return calculate(a,b,op)

#TOP LEVEL - dialogue.It captures everything and explains it to the user

def run_calculator():

    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        op = input("Enter Action (+,-,*,/): ")
        result = pars_and_calc(a,b,op)
        print(f"Result:{result}")
    except ValueError as e:
        print(f"Invalid data: {e}")
    except ZeroDivisionError:
        print("You can`t divide by zero!")

run_calculator()