from collections import Iterable,Iterator,Container
class bothIterAndNext:
    def __iter__(self):
        pass
    def __next__(self):
        pass
# a = isinstance(bothIterAndNext(), Iterable)
# print(a)
# b = isinstance(bothIterAndNext(), Iterator)
# print(b)

class onlyNext:
    def __next__(self):
        pass
# a = isinstance(onlyNext(), Iterable)
# print(a)
# b = isinstance(onlyNext(), Iterator)
# print(b)

class onlyIter:
    def __iter__(self):
        pass
# a = isinstance(onlyIter(), Iterable)
# print(a)
# b = isinstance(onlyIter(), Iterator)
# print(b)

# li = [1, 2, 3]
# li_iterator = iter(li)
# print(id(li_iterator))
# print(isinstance(li,Iterator))
# print(isinstance(li_iterator,Iterator))
# print(next(li_iterator))
# print(next(li_iterator))
# li_iterator = iter(li_iterator)
# print(next(li_iterator))
# print(id(li_iterator))

class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('justdopython.com')
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))

