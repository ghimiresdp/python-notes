import re

# compile
countries = ['USA', 'Japan', 'Angola', 'China', 'Algeria', 'Nepal', 'Argentina', 'Albania']

# a word that starts with A and ends with a
pattern = re.compile(r'^A\w*a$')

for country in countries:
    print(pattern.match(country))

# compile example 2

strings = ["0xaa", 'FA04', 'Ak45', 'As40', '0x5h', '0x56']

pat = re.compile(r'^(0x)?[0-9A-Fa-f]+$')

for st in strings:
    print(pat.match(st))

# search()
text = "Dear sir, I've emailed you last week regarding the assignment. I've also sent you another mail specifying the next assignment."

results = re.search(r'e?mail(ed)?', text)
print(results)

# match()
text = 'Dear sir'
print(re.match(r'[a-z]e\w+', text, re.I))
"""
# output
<re.Match object; span=(0, 4), match='Dear'>
"""

# # findall
countries = 'USA, Japan, Angola, China, Algeria, Nepal, Argentina, Albania'

print(re.findall(r'A[a-z]+a', countries))

"""
# Output

['Angola', 'Algeria', 'Argentina', 'Albania']
"""
