# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

basic_foods = ("fries", "burger", "kebab", "pizza", "nuggets")
for food in basic_foods:
    print(food)

# basic_foods[0] = "trout ala créme"
#     ~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

basic_foods = ("trout ala créme", "ketchup sweetened lobster", "kebab", "pizza", "nuggets")
for food in basic_foods:
    print(food)


