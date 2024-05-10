"""
calculates the root of x**n=a
>>> getn(2,4)
2
>>> getn(3,64)
4
>>> getn(2,64)
8
"""


def improve(update, close, x=1):
    while not close(x):
        x = update(x)
    return x


eps = 1e-5


def appro(x, y):
    dif = abs(x - y)
    return dif < eps


def newton(f, df):
    def nupdate(x):
        return x - f(x) / df(x)

    def nclose(x):
        return appro(f(x), 0)

    return improve(nupdate, nclose)


def mypow(n, x):
    k, ret = 0, 1
    while k < n:
        ret = ret * x
        k = k + 1
    return ret


def getn(n, a):
    def f(x):
        return mypow(n, x) - a

    def df(x):
        return mypow(n - 1, x) * n

    return newton(f, df)


getn(2, 4)
