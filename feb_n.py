def febbo(amount: int):
    a, b = 0, 1
    for __ in range(amount):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    leng = int(input('введите элементы: '))
    if leng > 0:
        for item in febbo(leng):
            print(item, end=', ')
    else:
        print(('Введите кол-во элементов > 0'))
