'''it is a built in data type in python which is used to store multiple items in a single variable. 
It is ordered, changeable, and allows duplicate values. 
Lists are defined by enclosing the items in square brackets [] and separating them with commas.'''

####String is immutable in python but list is mutable in python.

marks = [90, 85, 78, 92, 88]

student = ['karan',89,'male','delhi']
print(student) # it will print the list
student[0] = 'rohan' # we can change the value of list in python
str = 'karan'
print(str[0])
# str[0] = 'r' # we cannot change the value of string in python because it is immutable
# print(str)

len(student) # it will give the length of the list
print(student) # it will print the list
print(type(student)) # it will print the type of the list
print(student[0]) # it will print the first element of the list

'''List Slicing: It is used to access a range of elements in a list.
list_name[starting_indx:ending_indx]'''

marks = [85,50,78,92,88]
print(marks[1:4]) # it will print the elements from index 1 to index 3
print(marks[:3]) # it will print the elements from index 0 to index 2
print(marks[2:4]) # it will print the elements from index 2 to index 3
print(marks[-3:-1]) # it will print the elements from the third last to the second last

