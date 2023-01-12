# 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be
# simple, such as, “Hello Eric, would you like to learn some Python today?”

name = "lister"  # store string as variable
# concatenate strings and variables into single message, display var with first letter uppercase using .title method
print("Hello " + name.title() + ", Would you like your cold vindaloo sauce for breakfast?")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.

full_name = "david Lister"
print("with no methods " + full_name)
print("This upper method displays this " + full_name.upper())
print("lower method does this " + full_name.lower())
print("title method looks like this " + full_name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

philosopher = "john amos comenius"
print(philosopher.title() + " once said: 'If a man is to become a man, he must educate himself.'")

sec_name = "  Arnold Judas Rimmer  "
print(sec_name.rstrip())
print(sec_name.lstrip())
print(sec_name.strip())



