import operator

class Calculate:
    def __init__(self):
        self.numbers = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        self.operations = {'plus': operator.add, 'minus': operator.sub}
        self.val1 = ''
        self.val2 = ''
        self.op = ''
        self.res = 0

    def calc(self):
        self.res = self.operations[self.op](self.numbers.index(self.val1), self.numbers.index(self.val2))

    def request_operation(self):
        print('Welcome to this calculator!')
        print('It can add and subtract whole numbers from zero to five')
        self.val1 = input('Please choose your first number (zero to five): ')
        self.op = input('What do you want to do? plus or minus: ')
        self.val2 = input('Please choose your second number (zero to five): ')

    def is_params_valid(self):
        if (self.val1 in self.numbers
                and self.val2 in self.numbers
                and self.op in self.operations):
            return True
        return False

    def result_to_str(self):
        out = f'{self.val1} {self.op} {self.val2} equals'
        if (self.res < 0):
            out = f'{out} negative'
        out = f'{out} {self.numbers[abs(self.res)]}'
        return out

if __name__ == '__main__':
    c = Calculate()
    c.request_operation()
    if c.is_params_valid():
        c.calc()
        print(c.result_to_str())
