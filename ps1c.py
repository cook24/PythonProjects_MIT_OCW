
# Calculates payment needed to pay off debt in one year


# input variables
interest_rate = float(input('Enter interest rate as decimal: '))
original_balance = float(input('Enter balance as decimal: '))


# state variables
balance = original_balance
low_payment = balance / 12
high_payment = ((balance * (1 + (interest_rate / 12)) ** 12) / 12)


# use bisection search
while True:
    balance = original_balance
    monthly_payment = (low_payment + high_payment) / 2
    month_counter = 0

    # simulate year passing
    for m in range(1, 13):
        interest = round(balance * interest_rate / 12, 2)
        balance += interest - monthly_payment
        month_counter += 1

    if balance > 1:
        low_payment = monthly_payment

    elif balance < -1:
        high_payment = monthly_payment
    else:
        print('Result:')
        print('payment to pay in one year: ', round(monthly_payment, 2))
        print('months needed: ', month_counter)
        print('balance: ', round(balance, 2))
        break
