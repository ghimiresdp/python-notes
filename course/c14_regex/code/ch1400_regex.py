import re

# compile
countries = ['USA', 'Japan', 'Angola', 'China', 'Algeria', 'Nepal', 'Argentina', 'Albania']

# a word that starts with A and ends with a
pattern = re.compile(r'^A\w*a$')

for country in countries:
    print(pattern.match(country))


# findall
countries = 'USA, Japan, Angola, China, Algeria, Nepal, Argentina, Albania'

pattern = re.compile(r'A\w*a')
print(pattern.findall(countries))
