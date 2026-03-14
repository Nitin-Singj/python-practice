# LISTS
name = "harry"

# check karta hai string kis word se end ho rahi hai
print(name.endswith("rry"))

# kisi character ki kitni baar repetition hai
print(name.count("r"))

# first letter capital karta hai
print(name.capitalize())

# kisi word ka index batata hai
print(name.find("rr"))

# character replace karta hai
print(name.replace("r", "l"))
 #  LISTS METHOD 
l1 = [1,8,7,2,21,15]

# list ko ascending order me sort karega
l1.sort()
print(l1)

# list ko reverse karega
l1.reverse()
print(l1)

# end me value add karega
l1.append(8)
print(l1)

# kisi specific index par value insert karega
l1.insert(3,8)
print(l1)

# index ke basis par element remove karega
l1.pop(2)
print(l1)

# specific value remove karega
l1.remove(21)
print(l1)
# TUPLE
# tuple list jaisa hota hai lekin immutable hota hai (change nahi kar sakte)

a = (1,7,2)

print(a)

# kisi number ki frequency count karta hai
print(a.count(1))

# kisi value ka index batata hai
print(a.index(7))