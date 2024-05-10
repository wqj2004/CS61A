def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for ele in s:
        key = fn(ele)
        if grouped.get(key) != None:
            lst = grouped[key]
            if lst.count(ele) == 0:
                lst += [ele]
        else:
            grouped[key] = [ele]
    return grouped


def add_this_many(x, el, s):
    """Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    num = s.count(x)
    app = [el] * num
    s += app
    return s


def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for x in iterable:
        if fn(x) == True:
            yield x
    return


def merge(a, b):
    """
        >>> def sequence(start, step):
    ... while True:
    ... yield start
    ... start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    reta = next(a)
    retb = next(b)
    if reta < retb:
        last = reta
        reta = next(a)
    else:
        last = retb
        retb = next(b)
    yield last
    while 1:
        if reta < retb:
            if last == reta:
                reta = next(a)
                continue
            else:
                last = reta
                reta = next(a)
        else:
            if last == retb:
                retb = next(b)
                continue
            else:
                last = retb
                retb = next(b)
        yield last


def sequence(start, step):
    while True:
        yield start
        start += step


a = sequence(2, 3)
b = sequence(3, 2)
result = merge(a, b)
[next(result) for _ in range(10)]
