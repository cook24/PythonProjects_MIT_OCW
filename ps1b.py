#PS1B


# assigning variables to be used to calculate time to save down payment


#Input variables
total_cost = float(input("How much does your ideal house cost? "))
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("Enter % salary saved, as decimal:  "))
semi_annual_raise = float(input("Enter semi annual % raise, as decimal: "))


# Non-input variables
portion_down_payment = .25
current_savings = 0
r = .04
monthly_salary = annual_salary / 12
month_counter = 0


# Contingent variables
monthly_savings = monthly_salary * portion_saved
monthly_savings_growth = current_savings * (1 + (r / 12))
down_payment = portion_down_payment * total_cost


# increase month_counter and savings until savings >= down payment
while current_savings < down_payment:
    # increase annual salary by raise amount every six months
    # re-initialize monthly earnings and savings to reflect raise
    if month_counter != 0 and month_counter % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved
    month_counter += 1
    current_savings = current_savings * (1 + r / 12)
    current_savings += monthly_savings
print(f"Number of months: {month_counter}")
print(current_savings)

'''
for month in range(360):
    if current_savings < down_payment:
        month_counter += 1
        current_savings = current_savings * (1 + r / 12)
        current_savings += monthly_savings
    else:
        print(f"Number of months: {month_counter}")
        break
'''

