change = float(input("Change amount?"))
dollars = int(change)
cents = round(change - dollars) * 100

BILL_DENOMINATIONS = (20, 10, 5, 1)
for denomination in BILL_DENOMINATIONS:
    bills = dollars // denomination
    dollars %= denomination #dollars = dollars % 20
    if bills != 0:
        print(f"{bills} ${denomination} {'bill' if bills == 1 else 'bills'}")

COIN_DENOMINATIONS = {25: 'quarter', 10: 'dime', 5: 'nickel', 1: 'penny'}
for denomination in COIN_DENOMINATIONS:
    coins = coins // denomination
    cents %= denomination
    name = COIN_DENOMINATIONS[denomination]
    if coins != 0:
        print(f"{coins} ${name} {'' if coins == 1 else 's'}")

"""
$20
$10
$5
$1
quarters
dimes
nickles
pennies
"""