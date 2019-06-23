#################################################
### Part A: House Hunting
#################################################

# User Inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Variable Initialization

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
target_savings = total_cost * portion_down_payment

months = 0

while current_savings <= target_savings:
    current_savings = current_savings + ((current_savings * r)/12) + (monthly_salary * portion_saved)
#    print("Months:", months, "Current Savings:", current_savings)
    months += 1

print("Number of months:", months)
