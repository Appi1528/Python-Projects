HISTORY_FILE = "calculator_history.txt"

def show_history():
    file = open(HISTORY_FILE,'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No History Found!")

    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print("History Cleared!")

def save_to_history(equation, result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please enter in the format: number operator number")
        return 
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
    
    if int(result) == result:
        result = int(result)
    print(f"Result: {result}")
    save_to_history(user_input, result)


def main():
    print("Welcome to the Calculator with History!")
    while True:
        user_input = input("Enter calculation (e.g., 2 + 3) or 'history' to view history or 'clear' to clear history or 'quit' to exit: ")
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()          