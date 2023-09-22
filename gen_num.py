def gen_nums(n):
    count = 0
    num_start = 2
    inc = 1
    yield num_start
    while count < n - 1:
        num_start += inc
        for i in range(2, int(num_start ** 0.5) + 1):
            if num_start % i == 0:
                break
        else:
            inc = 2
            count += 1
            yield num_start


print(*gen_nums(10),sep='\n')
