
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")


operation = int(input("Enter choice for operation (1/2/3/4): "))
result = None
if operation == 1:
    result = first_number + second_number
elif operation == 2:
    result = first_number - second_number
elif operation == 3:
    result = first_number * second_number
elif operation == 4:
    if second_number == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = first_number / second_number
else:
    print("Invalid operation choice.")

if result is not None:
    print("Result:", result)
