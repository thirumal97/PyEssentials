# sample Input
# x = 3
# y = 4
# In this exercise, you must implement the rep_cat function. You are given two integers, x and y, as arguments.
# You must convert them into strings.
# The string value of x must be repeated 10 times and the string value of y must be repeated 5 times.
# Sample output
# '333333333344444'

def rep_concat(x, y):
    str_x = str(x)*10
    str_y = str(y)*4
    return str_x+str_y


if __name__ == '__main__':
    print(rep_concat(2,3))

