# © https://sudipghimire.com.np
"""
Default Parameters in functions

- default parameters are the parameters that has values assigned if it is not supplied
- default parameters always should be at last
- any non default parameters after default causes error
- default parameters are completely optional while calling
"""


# %%
def add(x, y, z=5):
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
