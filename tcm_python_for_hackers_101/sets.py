set1 = {"a", "b", "c"} #no order, no duplicates
print(set1)
print(type(set1))

# print(set1[0]) will error because sets arent ordered

set2 = {"a", "a", "a"} #no duplicates 
print(set2)
print(len(set2))

set3 = {"a", 0, True}
print(set3)

set4 = set(("b", 1, False))
print(set4)

set1.add("d")
print(set1)

set3.update(set4) #add multiple items, does not replace
print(set3) #0 comes from duplicate false

list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

set5 = {4, 5, 6}
set6 = set4.union(set5) #union does not modify original set
print(set6)

set4.remove(4)
print(set4) #will produce error if value is missing

set4.discard(4) #will not produce error if value is missing
print(set4)

print(set1)
set1.pop() #only desireable for deleting random data
print(set1)
