# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive
for num in range(1, 21):
    print(num)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

# numbers = list(range(1, 1_000_001))
# for numb in numbers:
#     print(numb)
#
# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))

print(sum(numbers))


