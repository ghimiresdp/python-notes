# https://docs.python.org/3/library/functions.html#filter

def is_even(num):
    return num%2==0

list_1 = [1,2,3,4,5,6,7,8,9,10]

list_2 = filter(is_even, list_1)

print(list(list_2))
