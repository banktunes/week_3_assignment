# -------------------------------
# 1. Update a Variable with a Function
# -------------------------------
# Create a function `update_name()` that assigns "Chuka Emeka" to `full_name`,
# then updates it to "Chuka Okeke" and returns it.

def update_name():
    full_name = "Chuka Emeka"
    full_name = "Chuka Okeke"
    return full_name
print(update_name())

# No.1 Answer Here


# 2. Float and Integer Sentence
# -------------------------------
# Create a function `bio_data()` that takes `height` and `age`
# and returns an f-string describing them. user keyword arguements in here
def bio_data(height,age):
    return f"I'm {age} years old of age and {height} meters tall"
print(bio_data(height=1.27,age=35)
      )
# No.2 Answer Here


# -------------------------------
# 3. Boolean Type Check
# -------------------------------
# Write a function `check_login_status()` that takes a boolean
# `is_logged_in` and returns its type. Use default arguement in here.

def check_login_status(is_logged_in=True):
    return type(is_logged_in)
print(check_login_status())
print(check_login_status(False)
      )
# No.3 Answer Here



# -------------------------------
# 4. Full Name Generator
# -------------------------------
# Create a function `full_name(first, last)` that returns the full name. 
def full_name(First,Last):
    return f"{First} {Last}"
print(full_name("First" , "Last"))

# No.4 Answer Here

# 5. Remainder Calculator
# -------------------------------
# Write a function `get_remainder(a, b)` that returns the remainder of a ÷ b.
def get_remainder(a,b):
    return a % b 
print(get_remainder(26,4)
      )

# No.5 Answer Here

# 6. Sum of Two Floats
# -------------------------------
# Write a function `add_floats(a, b)` that returns the sum of two float inputs.
def add_floats(a,b):
    return a + b 
print(add_floats(26,4)
      )
# No.6 Answer Here


# 7. Check If a Number is Greater Than or Equal
# -------------------------------
# Write a function `compare_numbers(a, b)` that returns True if a ≥ b.

def compare_number(a,b):
    return a >= b 
print(compare_number(10,5),(3,8)
      )

# 8. ID & Clearance Checker
# -------------------------------
# Write a function `access_granted(has_id, has_clearance)` that returns True if both are True.
def access_granted(has_id,has_clerance):
    return has_id and has_clerance
print(access_granted(True,True)
      )
    

# No.8 Answer Here


# 9. Pass or Connection Check
# -------------------------------
# Write a function `can_enter(has_pass, knows_manager)` that returns True if either is True.
def can_enter(has_pass,knows_manager):
    return has_pass or knows_manager
print(can_enter(True,True)
      )

# No.9 Answer Here


# 10. Reverse Access
# -------------------------------
# Write a function `reverse_access(can_enter)` that returns the opposite of the input boolean.
def reverse_access(can_enter):
    return not can_enter
print(reverse_access(True)
      )

# No.10 Answer Here

# 11. Reverse a Sentence (but not letters)
# -------------------------------
# Write a function `reverse_sentence(sentence)` that takes:
# "The boy is gone" ➝ returns "gone is boy The"

def reverse_sentence(sentence):
    words = sentence.split()         # Split the sentence into words
    reversed_words = words[::-1]     # Reverse the list of words
    reversed_sentence = ' '.join(reversed_words)   # Join the words back into a sentence
    return reversed_sentence 
print(reverse_sentence("The boy is gone")
      )
# No.11 Answer Here

# 12. Get All Odd Numbers from a List
# -------------------------------
# Write a function `get_odds(numbers)` that returns only odd numbers from the list.
# Use `filter` and `lambda`.

def get_odds(numbers):
     return list(filter(lambda x: x % 2 != 0, numbers))
print(get_odds([23,46,78,38,98,120,238,365,456])
      )
# No.12 Answer Here


# -------------------------------
# 13. Total Word Count from Multiple Sentences
# -------------------------------
# Write a function `total_word_count(*sentences)` that takes any number of strings
# and returns the total number of words.
def Total_word_count()


# No.13 Answer Here


 #14. Multiply All Items in List
# -------------------------------
# Write a function `product_of_list(numbers)` that returns the product (you are using multiplication here) of all items
# using `reduce` and a regular function (not lambda).
# No.14 Answer Here



# -------------------------------
# 15. Replace Vowels with "*"
# -------------------------------
# Write a function `censor_vowels(word)` that replaces all vowels (a, e, i, o, u)
# in the word with "*".

# Example: If "NaijaTech" was passed as an argument, you get the output: N**j*T*ch
# No.15 Answer Here


# ================================
# End of Final Boss Round 🧠🧠🧠
# ================================



