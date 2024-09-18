#Python script that will calculate a users finances based on user's inputted monthly income and expenses

#Prompt user for financial details
monthly_income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))

#Calculate monthly savings
monthly_savings = monthly_income - total_expenses

#Project annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are ", monthly_savings)
print("Projected savings after one year, with interest, is: ", projected_savings)