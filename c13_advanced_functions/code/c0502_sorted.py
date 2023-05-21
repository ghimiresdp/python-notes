# sorting in an ascending order
print(sorted([1, 4, 7, 2, 9, 5, 3]))

# sorting in an ascending order
print(sorted([1, 4, 7, 2, 9, 5, 3], reverse=True))


## Sorting the dictionary
person = {
    'name': 'John Doe',
    'age': 20,
    'occupation': 'student'
}
print(sorted(person))

# Sorting the dictionary to get the dictionary
print(sorted(person.items()))

print({k:v for k,v in sorted(person.items())})


# sorting with the key

students = [
    ('John', 2),
    ('Eve', 4),
    ('Jennifer', 3),
    ('Adam', 1)
]

print(sorted(students, key=lambda x: x[1]))
