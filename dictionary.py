'''Dictionaries are used to store data in key:value pairs. 
   A dictionary is a collection which is ordered, changeable and does not allow duplicates.'''

info = {
    "key" : "value",
    "name" : "Yash",
    "learning" : "python",
    "age" : 20,
    "marks" : [90, 85, 78, 92, 88],
    "topics" : ("python", "java", "c++")
}

print(info)
print(type(info)) # it will print the type of the dictionary

print(info["name"]) # it will print the value of the key "name"
print(info["age"]) # it will print the value of the key "age"   
print(info["marks"]) # it will print the value of the key "marks"
print(info["topics"]) # it will print the value of the key "topics"

info["name"] = "Yash" # we can change the value of the key "name" in the dictionary
info["surname"] = "Gupta" # we can add a new key:value pair in the dictionary
print(info)
