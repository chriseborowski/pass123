# import Python libraries

import random
import string
from pandas.io import clipboard

# generate random alphanumeric password

password_length = int(input("How many characters should there be in your password? "))

new_password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = password_length))

print(f"Your new {password_length}-character password is: {new_password}.")
copy_to_clipboard = input(f"Would you like to copy your password to the clipboard? (Y/N)")

# copy password to clipboard

if copy_to_clipboard.lower() == "y":
  clipboard.copy(new_password)
  print("Done! Your password is now copied to the clipboard.")
