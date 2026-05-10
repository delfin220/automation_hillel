class EvenIterator:
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration
        value = self.current
        self.current += 2
        return value
even_iterator = EvenIterator(10)

for i in even_iterator:
    print(i)