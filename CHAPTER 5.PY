# DICTIONARY
# dictionary key value pairs store karti hai

marks = {
    "Harry":100,
    "Rohan":56,
    "Shubham":23
}

# key se value access karte hai
print(marks["Harry"])
# DICTIONARY METHODS
a = {
    "name":"Harry",
    "from":"India",
    "marks":[92,98,96]
}

# dictionary ki keys show karega
print(a.keys())

# dictionary ki values show karega
print(a.values())

# key value pairs show karega
print(a.items())

# new data dictionary me add karega
a.update({"friends":"Rohan"})

print(a)
# SETS
# set unique values store karta hai

s = set()

s.add(1)
s.add(2)
s.add(3)

print(s)