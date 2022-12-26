def integers():
    i = 1
    while True:
        yield i
        i += 1


def squares():
    ints = integers()
    for i in ints:
        yield i ** 2


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


print(take(5, squares()))
