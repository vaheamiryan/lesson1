# lst = [3, 1, -7, -4, 9, -2]
# def negative(lst):
#
#     print(lst)
#     for i in range(len(lst)):
#         if lst[i]<0:
#             return i
#     return None
#
# print(negative(lst))
#
#


# def cities3():
#     lst = []
#     while True:
#         city = input('Enter city: ')
#
#         if city == '':
#             break
#
#         lst.append(city)
#
#     return lst
#
# x = cities3()
# print(x)

#
#
# employee = {'864-20': ['Arm', 'Spartyan'], '987-65': ['Vlad', 'Tundyan'], '100-01': ['Kiazh', 'Damyan']}
#
# print(employee['100-01'])
#

#
# days = {'Mo': 1, 'Tu': 2, 'W': 3}
#
# days2 = {'Tu': 8, 'Fr': 5}
#
# print(days.pop('Tu'))
# print(days)
# days['Tu'] = 2
# print(days)
# days.update(days2)
# print(days)
# print(days.items())
# print(days.keys())
# print(days.values())
#
#
# for i in days.items():
#     print(i)

# string = 'to be or not to be'
#
#
# def abc(w):
#     counters = {}
#     s = string.split()
#     for item in s:
#         if item in counters:  # increment item counter
#             counters[item] += 1
#         else:  # create item counter
#             counters[item] = 1
#
#
# print(counters)
# abc()

# phonebook = {
# 	'Arm':'56-78-90',
# 	'Vlad':'34-56-78',
# 	'Kiazh':'48-76-54'
# }
#
# def lookup():
#     while True:
#         print('Enter your name: ', end=' ')
#         name = input()
#         if name in phonebook:
#             print(phonebook[name])
# lookup()
#
#
#
# t = [('a', 10), ('c', 22), ('b', 1)]
# print(t)


x = open('romeo.txt', 'r')
y = x.read()
x.close()
print(y)
l = y.split()
print(l)
counters = {}
for item in l:
    if item in counters:  # increment item counter
        counters[item] += 1
    else:  # create item counter
        counters[item] = 1

lst = list()
for k, v in counters.items():
    lst.append((v, k))
lst.sort(reverse=True)
print(lst)
