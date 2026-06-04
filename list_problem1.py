'''WAP to ask the user to enter of their 3 favorite movies and store them in a list. Then print the list of movies.'''

movies = [] # creating an empty list to store the movies
mov1 = input("Enter your first favorite movie: ") # asking the user to enter their first favorite movie
mov2 = input("Enter your second favorite movie: ") # asking the user to enter their second favorite movie
mov3 = input("Enter your third favorite movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print("Your favorite movies are:", movies) 