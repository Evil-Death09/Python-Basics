'''WAP to check if a list contains a palindrome of elements.'''

list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy() # creating a copy of the original list
copy_list1.reverse() # reversing the copy of the list

if(list1==copy_list1):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

    