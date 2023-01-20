# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
# Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

places = ["Italy", "Sweden", "Spain", "Scotland", "England", "Croatia", "Germany"]

print(places)
print("This is an unsorted list.\n")

print(sorted(places))
print(" and this is an alphabetically sorted list\n")

print(places)
print("And this is unsorted list again.\n")

print(sorted(places, reverse = True))
print("this is reverse alphabetical order.\n")

print(places)
print("And this is unsorted list again.\n")

places.reverse()
print(places)
print("reverse method changes list order permanently")
places.reverse()

print(places)
print("apply once more the reverse method in order to sort the list back again")

print(len(places))

places.sort()
print(places)
print("this is permanently sorted by sort method")

places.sort(reverse=True)
print(places)

guests = ["karel", "martina", "kuba", "bára", "katka", "martin"]
print(f" initially, i had {str(len(guests))} guests invited for my birthday")

print(f" initially, i had {len(guests)} guests invited for my birthday")

# 3.10 omited due to redundancy

