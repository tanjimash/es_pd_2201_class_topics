

# print(type(x))


try:
    global x
    x = int(input('Enter Num: '))
except ValueError:
    print('Please insert an integer number!')



if x == 10:
    print('x is equal to 10')
else:
    print('x is not equal to 10')




