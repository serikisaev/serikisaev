class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __next__(self):
        result = self.first
        self.first, self.second = self.second, self.first + self.second
        return result

    def __iter__(self):
        return self

for i in Fibonacci():
    print(i)
    
    if i > 666:
        break
