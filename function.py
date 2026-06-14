def avg():
    a = int(input("enter a num: "))
    b = int(input("enter b num: "))
    c = int(input("enter c num: "))

    average = (a+b+c)/3
    print(average)

avg()

def goodDay(name,ending='Thank You'):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Yash")
goodDay("Yash","Thanks")