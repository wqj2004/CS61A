class MinList:
    """A list that can only pop the smallest element"""

    def __init__(self):
        self.items = []
        self.size = 0

    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size += 1
        cur = self.size - 1
        par = (cur + 1) // 2 - 1
        while par >= 0 and self.items[cur] < self.items[par]:
            temp = self.items[cur]
            self.items[cur] = self.items[par]
            self.items[par] = temp
            cur = par
            par = (cur + 1) // 2 - 1

    def pop(self):
        """Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        if self.size > 0:
            ret = self.items[0]
            self.items[0] = self.items[self.size - 1]
            self.items[self.size - 1] = ret
            self.size -= 1
            self.items.pop(self.size)
            cur = 0
            son = (cur + 1) * 2 - 1
            while son < self.size:
                if son + 1 < self.size and self.items[son + 1] < self.items[son]:
                    son = son + 1
                temp = self.items[cur]
                self.items[cur] = self.items[son]
                self.items[son] = temp
                cur = son
                son = (cur + 1) * 2 - 1

            return ret
        return 0


m = MinList()
m.append(4)
m.append(2)
print(m.size)
print(m.pop())
print(m.pop())
print(m.size)


m = MinList()
m.append(100)
m.append(4)
print(m.pop())
m.append(-100)
print(m.pop())
m.append(1)
m.append(5)
m.append(0)
m.append(7)
m.append(-2)
print(m.pop())
print(m.pop())
print(m.size)
