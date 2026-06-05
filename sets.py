'''Set is a collection of unique elements. 
   It is unordered and mutable but its elements are immutable.'''

collection = {5,2,3,4,1,"hello","world",True,False,2,3,4,5}
print(collection)
# Output: {False, True, 1, 2, 3, 4, 5, 'hello', 'world'}
print(type(collection))
print(len(collection))

#For empty set we have to use set() function
empty_set = set()
print(empty_set)

