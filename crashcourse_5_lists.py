# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

crew = ["lister", "rimmer", "kryten", "cat", "kochanski"]
print(crew[0].title())
print(crew[1].title())
print(crew[2].title())
print(crew[3].title())
print(crew[4].title())

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name.

print("Hello, " + crew[0].title() + ", would you like to practice your guitar today?")
print("Hello, " + crew[1].title() + ", how is your collection of telegraph columns of 20th century coming along?")
print("Hello, " + crew[2].title() + ", we have lot of clothing that needs some ironing")
print("Hello, " + crew[3].title() + ", you are looking really fine today!")
print("Hello, " + crew[4].title() + ", would you like goat cheese with pieces of pineapple?")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

transport_list = ["starbug", "red dwarf", "cat fleet"]
print("I would like to command a feral " + transport_list[2] + "someday.")
# i shall not print other statements as the exercise is the same as previous one

