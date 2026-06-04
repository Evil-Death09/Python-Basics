student = {
    "name": "yash",
    "subjects" : {
        "maths" : 96,
        "phys" : 89,
        "chem" : 92
    }
}

print(student.keys()) # it will print the keys of the dictionary
print(list(student.keys())) # it will print the keys of the dictionary in a list
print(len(student))

print(student.values()) # it will print the values of the dictionary
print(list(student.values())) # it will print the values of the dictionary in a list

print(student.items()) # it will print the key:value pairs of the dictionary
print(list(student.items())) # it will print the key:value pairs of the dictionary in a list

print(student.get("name")) # it will print the value of the key "name"
print(student.get("name")) # it will print the value of the key "name"

student.update({"city" : "delhi", "age" : 20}) 
print(student)