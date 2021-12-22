import random
import string

upper_chars = string.ascii_uppercase
lower_chars = string.ascii_lowercase
digit_chars = string.digits
symbol_chars = string.punctuation

print("Enter the amount of upper case character you required in password")
uc=int(input())
print("Enter the amount of lower case character you required in password")
lc=int(input())
print("Enter the amount of special character you required in password")
sc=int(input())
print("Enter the amount of digit you required in password")
dc=int(input())

k=uc+lc+sc+dc

print("Your password lenght is = " + str(k))
random_upper_chars = "".join(random.sample(upper_chars, int(uc)))
random_lower_chars = "".join(random.sample(lower_chars, int(lc)))
random_digit_chars = "".join(random.sample(digit_chars, int(dc)))
random_symbol_chars = "".join(random.sample(symbol_chars, int(sc)))


pass_string = (
    random_upper_chars + random_digit_chars + random_lower_chars + random_symbol_chars
)

pass_string = "".join(random.sample(pass_string, len(pass_string)))
print("Password is = " +str(pass_string))

