class PrimeNumbers:
    def __init__(self, second):
        self.second = second

    def checkprimenumber(self,n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True

    def __iter__(self):
        yield 2
        if self.second>2:
            for n in range(2,self.second):
                if self.checkprimenumber(n):
                    yield n
                    
for n in PrimeNumbers(100):
        print(n)
