# © https://sudipghimire.com.np
"""
Default Parameters in functions

- default parameters are the parameters that has values assigned if it is not supplied
  while calling the function
- default parameters always should be at last
- any non default parameters after default causes error
- default parameters are completely optional while calling
"""


# %%
def add(x, y, z=0):
    return x + y + z


print(add(3, 4, 10))

print(add(3, 4))


# %% example use case
def greet(key, lang='en'):
    dict_1 = {
        'hello': {
            'en': 'Hello',
            'fr': 'Bonjour',
            'np': 'नमस्कार',
            'jp': 'こにちは'
        },
        'bye': {
            'en': 'Bye',
            'fr': 'au revoir',
            'np': 'फेरी भेटौला',
            'jp': 'さよなら'
        }
    }
    print(dict_1[key][lang])


greet('hello', 'fr')
greet('hello', 'jp')
greet('hello')


# %% power of the number with default value 2
def power(x, y=2):
    return x ** y


print(power(10))
print(power(10, 4))

# %%
lst = [1, 2, 3, -3, -5, 7, 6, -4, 8, -8]
new_list = []
for (index, value) in enumerate(lst):
    for x in lst[index + 1:]:
        tmp_sum = x + value
        for n in lst:
            if tmp_sum + n == 0:
                new_list = [*new_list, [value, x, n]]
print(new_list)
