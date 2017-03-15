# # f = open('tobe.txt', 'w')
# # f.write('to be or not to be')
# # f.close()
# # f = open('tobe.txt', 'r')
# # y = f.read()
# # print(y)
#
#
# def file('tobe.txt'):
#



# def histogram(x):
#     for i in x:
#         print(i*'*')
# x=[4, 7, 9]
# histogram(x)



def histogram(x):
    f = open('010203.txt', 'w')
    for i in x:
       x = f.write(i * '*'+ '\n')

    f.close()

x=[4, 7, 9]
histogram(x)
