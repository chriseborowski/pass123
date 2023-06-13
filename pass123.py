# import Python libraries

import random
import string

# generate random alphanumeric password

password_length = 20

new_password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = password_length))

print(str(new_password))

# copy password to clipboard



# display password on page
