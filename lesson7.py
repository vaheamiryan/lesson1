# squares = []
# for x in range(10):
#     squares.append(x ** 2)
#
# print(squares)

# squares = [x**2 for x in range(10) if x>4]
# print(squares)
#
# fruits = ['  banana', '  raspberry ', ' grapefruit  ']
# fruits = [fruit.strip().upper() for fruit in fruits]
# print(fruits)
#
# nums = [(x, x**3) for x in range(6)]
# print(nums)

# num = sum([x for x in range(1,101) if x%2==0])
# print(num)

import requests



def requests.get(x):\
    start = 1329
    end = 1423

    text = res.text
    count=0
    for symbol in text :
        if start <= ord(symbol) <= end:
            print(symbol, ord(symbol))
            count +=1

    print (count)

requests('https://www.news.am/arm/')
# for i in range(start, end + 1):
#     print(format(i, 'X'), end=' ')  #hex
#     print(i, end=' ')               #dec
#     print(chr(i))              #letter



