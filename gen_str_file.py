from pprint import pprint as вывод

name = ['Alex', 'Mark', 'Mars']
bet = [90000, 100000, 100000]
prize = ['10.25%', '12.50%', '11.5%']

result = {name: (bet * float(per.strip('%')) / 100) for name, bet, per in zip(name, bet, prize)}
вывод(result)
