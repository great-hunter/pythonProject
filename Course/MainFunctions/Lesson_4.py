set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(len(set1))

set1.add(10)
print(set1)

set1.remove(10)
print(set1)

#set1.remove(5)
set1.discard(5)
print(set1)

print("--------")
print(set1 == set2)
print(set1 <= set2)
print(set1 >= set2)

print("--------")
set1 = {2, 3, 4}
set2 = {1, 2, 3}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

set1.clear()
set2.clear()
print(set1)
print(set2)