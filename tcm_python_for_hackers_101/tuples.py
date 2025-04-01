tuple_items = ("apple", "banana", "cherry")
print(tuple_items)
print(type(tuple_items))

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

tuple_repeat = ('Combine!',) * 4
print(tuple_repeat)
print(type(tuple_repeat))

mixed_tuple = ("A", 1, ("A",1))
print(mixed_tuple)
print(type(mixed_tuple))

tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))
print(type(tuple_combined))

item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

print("banana" in tuple_items)
print("cherry" in tuple_items)
print("item4" in tuple_items)

print(tuple_items.index("cherry"))

tuple_items = ("item1", "item2", "item3")
print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

print(len(tuple_items))

print(tuple_items[-1])
print(tuple_items[-2])

print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-3:-1])

string1 = "I am a string!"
print(string1[0:4])
print(string1[-1])
