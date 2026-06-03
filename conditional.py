#Syntex::
#if(condition):
#   statement1
#elif(condition):
#   statement2
#else:
#   statementN.....

age = int(input("Enter your age: "))

if(age>=18):
    print("can vote and apply for licence")
    print("can drive")
elif(age>=16):
    print("can apply for licence")
else:
    print("ghar betho ")

#grade students based on marks
marks = int(input("Enter your marks: "))
if(marks>=90):
    print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B")
elif(marks>=70 and marks<80):
    print("Grade C")
else:
    print("Grade D")