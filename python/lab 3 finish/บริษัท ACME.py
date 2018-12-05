# input
amount_buy = float(input("Enter buying amount: "))


# process

if (0 <= amount_buy < 1000):
    amount_due = amount_buy
elif (amount_buy>=1000 and amount_buy<3000):
    amount_due = (9*amount_buy/10)
else:
    amount_due = (85*amount_buy/100)


# output
print('Amount due after discount is %.2f baht.' % amount_due)
