# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits 
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"


def validation(some_string):
    password_is_valid = True
    if len(some_string) < 6 or len(some_string) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not some_string.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    digits_counter = 0
    for character in some_string:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    return password_is_valid

some_password = input()
if validation(some_password):
    print("Password is valid")
