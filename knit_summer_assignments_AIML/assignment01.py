'''Build a simple command line quiiz game in python inspired by KBC using loops,conditional,and basic data structure'''

print("Welcome to KBC!")

list = [{"Question":"PM of India",
         "Options":["A. Narendra Modi","B. Rahul Gandhi","C. Arvind Kejriwal","D. Manmohan Singh"],
         "Answer":"A","Prize":1000,
         "Lifeline":"50-50"},
         {"Question":"Capital of India",
          "Options":["A. Mumbai","B. Delhi","C. Kolkata","D. Chennai"],
          "Answer":"B","Prize":2000,},
          {"Question":"National Animal of India",
           "Options":["A. Lion","B. Tiger","C. Elephant","D. Peacock"],
           "Answer":"B","Prize":3000,},
           {"Question":"National Bird of India",
            "Options":["A. Peacock","B. Sparrow","C. Crow","D. Pigeon"],
            "Answer":"A","Prize":4000,},
            {"Question":"National Flower of India",
             "Options":["A. Lotus","B. Rose","C. Sunflower","D. Marigold"],
             "Answer":"A","Prize":5000,}]
score = 0
for i in list:
    print(i["Question"])
    for j in i["Options"]:
        print(j)
    answer = input("Enter your answer: ").upper()
    if answer == i["Answer"]:
        score += i["Prize"]
        print("Correct! Your score is",score)
    else:
        print("Wrong! Your score is",score)
        break
    print("You are a crorepati")