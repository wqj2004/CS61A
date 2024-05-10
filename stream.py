"""
很复杂的一个题目,花了好大力气+画了个图才搞清楚它在干什么，还是有点猎奇了
总的来说就是要理解python在函数调用的时候和环境有关，一个函数返回后它的环境是仍然存在的
然后用filter就是可以利用not_div函数分很多层filter,每经过一个not_div筛选后都生成一个新的filter，
当然最原始的是正整数序列
整体算法思想就是通过很多层filter,找到了一个和当前任意一个质数都不整除的数(通过层层filter获得)，然后把这个数加到
primes序列里，然后再为它构造一个not_div函数


"""


class Stream:
    """A lazily computed linked list."""

    class empty:
        def __repr__(self):
            return "Stream.empty"

    empty = empty()

    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), "compute_rest must be callable."
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return "Stream({0}, <...>)".format(repr(self.first))


def integer_stream(first):
    def compute_rest():
        return integer_stream(first + 1)

    return Stream(first, compute_rest)


def filter_stream(fn, s):
    if s is Stream.empty:
        return s

    def compute_rest():
        return filter_stream(fn, s.rest)

    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()


def first_k_as_list(s, k):
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k - 1
    return first_k


def primes(pos_stream):
    def not_divible(x):
        return x % pos_stream.first != 0

    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))

    """
    当然，这个算法的思想也很简单，就是原始的是一个pos_stream流，通过一步一步的filter_stream把所有not_divible
    无法通过的数全都筛掉。
    而且由于python的环境特性，这个算法的正确性是可以得到保障的，因为每在primes流里面加了一个新的质数
    前面的质数的所有倍数被筛掉都被筛掉了，这是通过filter_stream函数的逻辑实现的
    """

    return Stream(pos_stream.first, compute_rest)


prime_numbers = primes(integer_stream(2))
first_k_as_list(prime_numbers, 7)
