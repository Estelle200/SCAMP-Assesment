def fibonacci_series():
    a, b = 0, 1
    n = int(input('Enter a number: '))
    if n <= 0:
        print('Enter a positive number')
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for number in range(2, n):
            c = a + b
            print(c)
            a, b = b, c
fibonacci_series()





