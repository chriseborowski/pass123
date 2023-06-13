# import Python libraries

import random
import string

# generate random alphanumeric password

password_length = int(input("How many characters should there be in your password? "))

new_password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = password_length))

print(f"Your new {password_length}-character password is: {new_password}.")


# copy password to clipboard



# display password on page
