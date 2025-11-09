income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Annual interest rate
interest_rate = 0.05

# Projected annual savings
yearly_savings = monthly_savings * 12
projected_savings = yearly_savings + (yearly_savings * interest_rate)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
