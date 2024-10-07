def get_numbers():
    numbers = []
    while True:
        try:
            num = float(input("Enter a number (or 'done' when finished): "))
            numbers.append(num)
        except ValueError:
            if len(numbers) < 2:
                print("Please enter at least two numbers.")
                continue
            break
    return numbers

def choose_operation():
    while True:
        operation = input("Choose operation (+ for addition, - for subtraction): ")
        if operation in ['+', '-']:
            return operation
        print("Invalid operation. Please choose + or -")

def calculate_result(numbers, operation):
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

def calculator():
    while True:
        # Input Numbers
        numbers = get_numbers()
        
        # Choose Operation
        operation = choose_operation()
        
        # Calculate Result
        result = calculate_result(numbers, operation)
        
        # Display Result
        print(f"Result: {result}")
        
        # Ask if user wants to perform another calculation
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    print("Welcome to the Calculator!")
    calculator()
    print("Thank you for using the Calculator!")
