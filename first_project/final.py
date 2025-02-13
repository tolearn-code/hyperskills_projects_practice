# Write your code here
print('''Prices:
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2''')
prices_dict = {
        'Bubblegum': 202,
        'Toffee': 118,
        'Ice cream': 2250,
        'Milk chocolate': 1680,
        'Doughnut': 1075,
        'Pancake': 80
    }

amount = 0
print("Earned amount:")
for item, price in prices_dict.items():
    print(f'{item}: ${price}')
    amount += price
print()

print(f'Income: ${amount}')

expense_staff =int(input('Staff expenses:\n'))
expense_other =int(input('Other expenses:\n'))
net_income = amount - expense_other - expense_staff
print(f"Net income: ${net_income}")