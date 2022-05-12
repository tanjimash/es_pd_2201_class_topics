#  Write a Python program to reverse a string.


sample_string = "1234abcd"

list_var = []

for i in range(len(sample_string)-1, -1, -1):
    list_var.append(sample_string[i])

x = ''.join(list_var)
print(x)

# b = sample_string[::-1]
# print(b)
