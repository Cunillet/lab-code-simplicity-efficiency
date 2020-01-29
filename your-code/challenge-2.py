import random
from string import ascii_letters as letters

class StringGenerator:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0
        self.count = 0
    
    def get_rand_letter(self):
        return random.choice(str.lower(letters))

    def get_rand_digit(self):
        return random.randint(0, 9)
    
    def get_rand_str(self):
        if bool(random.getrandbits(1)):
            return self.get_rand_letter()
        return str(self.get_rand_digit())

    def generate_rand_str(self, l):
        return ''.join([self.get_rand_str() for i in range(l)])

    def request_basics(self):
        self.minimum = int(input('Enter minimum string length: '))
        self.maximum = int(input('Enter maximum string length: '))
        self.count = int(input('How many random strings to generate? '))
    
    def get_requested_str(self):
        for _ in range(self.count):
            l = random.randint(self.minimum, self.maximum)
            print(self.generate_rand_str(l))


if __name__ == '__main__':
    sg = StringGenerator()
    sg.request_basics()
    sg.get_requested_str()
