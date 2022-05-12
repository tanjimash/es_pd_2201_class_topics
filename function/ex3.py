# Write a Python function to multiply all the numbers in a list.

from operator import mul


list_var = [8, 2, 3, -1, 7]

def multiplication_val(number_list):
    x = 1
    for i in number_list:
        x = x * i
    return x



print('Multiplcation Result:', multiplication_val(list_var))