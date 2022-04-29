import re

str_1 = 'John, Jane, Jennifer, Joan, Jon, Adam, Eve'


print(re.findall(r'J\w*n', str_1))
