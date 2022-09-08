annual_interest =float(input('enter interest as decimal: '))
start_balance = int(input('enter card balance: '))
balance = start_balance
payment = 10
total_paid = 0
month_counter = 0


while balance > 0:
    payment += 10
    month_counter = 0
    balance = start_balance
    total_paid = 0
    for m in range(1, 13):
        interest_accrued = round(((annual_interest / 12) * balance), 2)
        principal_paid = round((payment - interest_accrued), 2)
        balance = round((balance - principal_paid), 2)
        total_paid += payment
        month_counter += 1

print(f'balance after one year: {balance}')
print(f'payment: {payment}')
print(f'total_paid: {total_paid}')
print(f'months: {month_counter}')
