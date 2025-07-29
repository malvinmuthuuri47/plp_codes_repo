def is_valid_operation(op, num1, num2):
	if op in ('/', '%') and num2 == 0:
		print("Error: Cannot divide or mod by zero.")
		return False
	return True


def calculate(num1, op, num2):
	operations = {
		'+': lambda a, b: a + b,
		'-': lambda a, b: a - b,
		'*': lambda a, b: a * b,
		'/': lambda a, b: a / b,
		'%': lambda a, b: a % b,
		'**': lambda a, b: a ** b
	}

	if op not in operations:
		print("Error: Unsupported operator.")
		return None

	return operations[op](num1, num2)

def main():
	print("=== Calculator App ===")

	try:
		num1 = float(input("Enter the first number: "))
		op = input("Enter an operator (+, -, * - Multiplication, / - Division, % - Remainder, ** - Square ): ")
		num2 = float(input("Enter the second number: "))

		if not is_valid_operation(op, num1, num2):
			return

		result = calculate(num1, op, num2)
		if result is not None:
			print(f"{num1} {op} {num2} = {result}")

	except ValueError:
		print("Error: Please enter valid numbers.")

if __name__ == "__main__":
	main()
