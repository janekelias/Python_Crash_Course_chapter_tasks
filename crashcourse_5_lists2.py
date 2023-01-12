# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting them to dinner

guests = ["karel", "martina", "kuba", "bára", "katka", "martin"]
for guest in guests:
    print(f"Hello {guest.title()}, i would like to invite you to my birthday party!")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.

print(f"\nI just heard that {guests[5].title()} is unable to come, what a shame.\n")
guests[5] = "jirka"

for guest in guests:
    print(f"Hello {guest.title()}, i would like to invite you to my rescheduled birthday party!")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.

print(f"\n Hello, guests, im afraid i have another change, i have found bigger dinner table at the restaurant, so i will"
      f" add another three guests to our party!\n")

guests.insert(0, "olda")
guests.insert(2, "zpytihněv")
guests.append("iveta")

for guest in guests:
    print(f"Hello {guest.title()}, i would like to invite you to my big birthday party!")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

print(f" unfortunately, an pandemic broke out and only two people are able to visit me at my home.")

while len(guests) > 2:
    quarantine = guests.pop()
    print(f"Im sorrry {quarantine}, im unable to invite you to my party due to the law restrictions.\n")
print("\n\nIt looks like only two people are remaining, we can schedule at least a small party.\n\n")

for guest in guests:
    print(f"Hello {guest.title()}, i would like to invite you to my small birthday party!")

