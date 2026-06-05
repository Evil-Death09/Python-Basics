collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("hello")
collection.add((1,2,3))
print(collection)

collection.remove(2) # removes the specified element from the set. If the element is not found, it raises a KeyError.
print(collection)

collection.pop() # removes and returns an arbitrary element from the set.
print(collection)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2)) #combines all unique elements from both sets
print(set1.intersection(set2)) #returns a new set containing only the elements that are present in both sets
print(set1.difference(set2)) #returns a new set containing only the elements that are present in the first set but not in the second set

print(len(collection))
collection.clear() # removes all elements from the set, leaving it empty
print(collection)
print(len(collection))



