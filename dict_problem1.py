'''WAP to enter marks of 3 subjects from the user and store it in a dictionary. 
Start with an empty dictionary and add the marks one by one.Use subject names as keys and marks as values. Finally, print the dictionary.'''

marks = {}

x = int(input("Enter marks of sub1: "))
marks.update({"sub1":x})

x = int(input("Enter marks of sub2: "))
marks.update({"sub2":x})

x = int(input("Enter marks of sub3: "))
marks.update({"sub3":x})

print(marks)