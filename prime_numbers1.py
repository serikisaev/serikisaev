class PrimeNumbers:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __next__(self):
        result = self.first
        for i in range(self.first, self.second):
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    print(i)
                    
    def __iter__(self):
        return self
                     
PrimeNumbers(2, 100)
