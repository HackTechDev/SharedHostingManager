import crypt
import string
import random

class Password:
    value = ""

    def __init__(self):
        self.value = ""

    def generateRandomPassword(self, size):
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])

    def generateEncodedPassword(self, password):
        return crypt.crypt(password, "22")

    def display(self):
        print(self.value)
