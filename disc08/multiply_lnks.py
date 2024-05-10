class Link:
    """A linked list.
    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3,Link(5,Link(4)))))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link != Link.empty:
        if f(link.first) == True:
            yield link.first
        link = link.rest


def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3,Link(5,Link(4)))))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    if f(link.first):
        yield link.first

    yield from filter_link(link.rest, f)  # yield from 这个用法就很屌啊


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    first = 1
    newlst = []
    for link in lst_of_lnks:
        if link == Link.empty:
            return Link.empty
        first *= link.first
        newlst += [link.rest]
    return Link(first, multiply_lnks(newlst))


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
e = Link(61, Link(37, Link(24, Link(98, Link(46, Link(55))))))
f = Link(59, Link(414, Link(4, Link(7, Link(12, Link(17, Link(8, Link(18))))))))
g = Link(2, Link(41, Link(12, Link(5, Link(1, Link(7, Link(19, Link(23, Link(47)))))))))
p = multiply_lnks([a, b, c])
p.first
p.rest.first
p.rest.rest.rest is Link.empty
