def countdown(n):
    if n <= 0:
        print('Blustoff')
    else:
        print(n)
        countdown(n - 1)


#


def vertical(n):
    '''prints digits of
    n vertically
    '''
    if n < 10:
        print(n)
    else:
        vertical(n // 10)
        print(n % 10)


#


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


#print(factorial(5))


def cheers():
    n = int(n)
    if n == 0:
        print('Hurray!!!')
    else:
        print('hip', end='')


#print(cheers(5))
if __name__ == '__main__':
    countdown(5)
    vertical(3154)





