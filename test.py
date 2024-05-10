def realanswer(n):
    k = 1
    ret = 0
    while k <= n:
        ret += 1 / (2 * k - 1)
        k += 1
    return ret


def C(n, k):
    child = 1
    mother = 1
    cou = 0
    while cou < k:
        child *= n - cou
        mother *= cou + 1
        cou += 1
    return child / mother


def myans(n):
    k = 1
    ans = 0
    while k <= n:
        ans += C(2 * n - 2 * k, n - k) * 2 ** (2 * k - 1) / (C(2 * n, n) * k)
        k += 1
    return ans


n = 50
ra = realanswer(n)
ma = myans(n)
print(ra)
print(ma)
print("eps:{0}".format(abs(ra - ma)))
