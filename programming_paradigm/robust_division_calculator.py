def safe_divide(numerator,denominator):
	try:
		num1 = float(numerator)
		num2 = float(denominator)

	except ValueError:
		return "Error: Please enter numeric values only."

	try:
		result = num1/num2

	except ZeroDivisionError:
		return "Error: Cannot divide by zero."

	return f"The result of the division is {result}"
