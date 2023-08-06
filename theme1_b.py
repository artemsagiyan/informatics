class NeighbouringNumbers:
    def __init__(self, num):
        self.num = num

    def print_neighbours(self):
        print('The next number for the number', self.num,  'is',  self.num + 1, end='.\n')
        print('The previous number for the number', self.num, 'is', self.num - 1, end='.\n')
