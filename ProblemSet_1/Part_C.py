#################################################
### Part C: Finding the right amount to save away
#################################################

# User Inputs

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

# Variable Initialization

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
semi_annual_raise = 0.07
total_cost = 1000000
target_savings = total_cost * portion_down_payment

months = 0

while current_savings <= target_savings:
    if months > 0 and months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary/12
    
    current_savings = current_savings + ((current_savings * r)/12) + (monthly_salary * portion_saved)
#    print("Months:", months, "Current Savings:", current_savings)
    months += 1

print("Number of months:", months)
