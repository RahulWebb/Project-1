# import string
# import random

# if __name__ == "__main__":
#     s1 = string.ascii_lowercase
#     s2 = string.ascii_uppercase
#     s3 = string.digits
#     s4 = string.punctuation
#     plen = int(input("Enter password length: "))
#     s = []
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#     print("Your password: ", end="")
#     print("".join(random.sample(s, plen)))

#   ***********      OR     *************

import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
length = int(input("Enter password length: "))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print("Your password: ", end="")
# print("".join(random.sample(s, length)))
print("your password:" ,"".join(random.sample(s, length)))

