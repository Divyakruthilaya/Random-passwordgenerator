import random
import string
length_password =int(input("Enterthe length of the password"))
password=string.ascii_letters+string.digits+string.punctuation
a ="".join(random.sample(password,length_password))
print(f"your password is {a}")