# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# •	 Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# •	 Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

guests = ["karel", "martina", "kuba", "bára", "katka", "martin"]
for guest in guests:
    print(f"Hello {guest.title()}, i would like to invite you to my birthday party!")

print(f"The first three persons on the list are {guests[:3]}")

print(f"The persons in the middle of the list are {guests[2:4]}")
print(f"Last three persons on the list are {guests[3:6]}")



crewmen = ["cat","Kryten", "holly", "tar'qa dhal"]
crew_old = crewmen[:]
print(crew_old)
crew_old.append("rimmer")
crewmen.append("kristine")

for crew in crewmen[:4]:
    print(f"my favourite crewman is {crew}")
print("\nold crewmen are:")
for oldie in crew_old:
    print(oldie)


