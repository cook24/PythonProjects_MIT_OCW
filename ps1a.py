
# 6.00
# problem set 1
# problem 1


# input variables
balance = int(input('Please enter the balance on your card: '))
payment_rate = float(input('Please enter the min payment rate as decimal: '))
annual_interest = float(input('Please enter the interest rate as decimal: '))


'''
# assumptions
balance = 5000
payment_rate = .02
annual_interest = .18
'''

# formulas
payment = payment_rate * balance
interest_accrued = (annual_interest / 12) * balance
principal_paid = payment - interest_accrued 
remaining_balance = balance - principal_paid


# each formula is written in the loop so that they can compute without changing
# the balance prior to being subtracted/added, as in the test cases
total_paid = 0

for m in range(1, 13):
    print('month', m)
    payment = round((payment_rate * balance), 2)
    print('payment:', payment)
    interest_accrued = round(((annual_interest / 12) * balance), 2)
    print('interest accrued:', interest_accrued)
    principal_paid = round((payment - interest_accrued), 2)
    print('principal paid:', principal_paid)
    balance = round((balance - principal_paid), 2)
    print('balance:', balance)
    total_paid += payment
    print('total paid:', round((total_paid), 2))
    print()


