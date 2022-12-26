class ReverseIter:
    def __init__(self, collection):
        self.data = collection
        self.index = len(self.data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


for each in ReverseIter([10, 54, 12, 0]):
    print(each)
