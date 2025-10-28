print("----- Simple Calculator -----")

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

# Performing operations
if choice == '1':
    result = num1 + num2
    print(f"\n✅ Result: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"\n✅ Result: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"\n✅ Result: {num1} × {num2} = {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\n✅ Result: {num1} ÷ {num2} = {result}")
    else:
        print("\n⚠️ Error: Cannot divide by zero!")
else:
    print("\n❌ Invalid Input! Please choose a valid operation.")
