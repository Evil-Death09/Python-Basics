'''Print the elements of the following list using loop'''
'''[1,4,9,16,25,36,49,64,81,100]'''

i =1
list = []
while i<=10:
    list.append(i**2)
    i += 1
print(list)

'''Search for a number x in this tuple using loop'''
tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number to search in the tuple: "))
i = 0
while i<len(tup):
    if tup[i]==x:
        print(x,"is found in the tuple at index",i)
    else:
        print("finding....")
    i += 1 
else:
     print(x,"is not found in the tuple")

