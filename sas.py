from pprint import pprint as pp

names = ['Илья', 'Иван', 'Игнат']
bet = [100000, 200000, 150000]
premium = ['10.25%', '15.50%', '8.75%']

result = {name: (bet * float(percentage.strip('%')) / 100) for name, bet, percentage in zip(names, bet, premium)}
pp(result)