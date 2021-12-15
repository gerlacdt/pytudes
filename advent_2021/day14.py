import utils

from collections import deque, Counter, namedtuple


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "{} -> {}".format(self.data, self.next)


class DoubleLinkedList:
    def __init__(self, arr=[]):
        self.head: Node = None
        self.tail: Node = None

        for item in reversed(arr):
            self.prepend(item)

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        result = self.current
        self.current = self.current.next
        return result

    def prepend(self, data):
        if not self.head and not self.tail:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node

    def insert_after(self, current: Node, data):
        if not self.head and not self.tail:
            raise RuntimeError("Cannot insert afer non-existent node.")
        if current == self.tail:
            newNode = Node(data, current, None)
            current.next = newNode
            self.tail = newNode
        else:
            tmp = current.next
            newNode = Node(data, current, current.next)
            current.next = newNode
            tmp.prev = newNode

    def toList(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def toListRev(self):
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def __repr__(self):
        return "{}".format(self.head)


def getInput():
    return utils.Inputstr("14")


def getPolymer(text):
    lines = text.splitlines()
    template = lines[0]
    pairs = {}
    for i in range(2, len(lines)):
        pair = lines[i].split("->")
        pairs[pair[0].strip()] = pair[1].strip()
    return template, pairs


def polymerize(template, pairs, steps=10):
    polymer = DoubleLinkedList(list(template))
    for i in range(steps):
        print("step: {}".format(i))
        current = polymer.head.next
        while current:
            key = current.prev.data + current.data

            if key in pairs:
                val = pairs[key]
                polymer.insert_after(current.prev, val)
                current = current.next
            else:
                current = current.next

    counts = Counter(polymer.toList()).values()
    return max(counts) - min(counts), "".join(polymer.toList())


example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def test_getPolymer():
    template, pairs = getPolymer(example)
    assert template == "NNCB"
    assert len(pairs) == 16


Case = namedtuple(
    "Case",
    ["steps", "expected", "p"],
)


def test_polymerize_example():
    template, pairs = getPolymer(example)
    cases = [
        Case(1, 1, "NCNBCHB"),
        Case(2, 5, "NBCCNBBBCBHCB"),
        Case(3, 7, "NBBBCNCCNBBNBNBBCHBHHBCHB"),
        Case(4, 18, "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"),
        Case(10, 1588, ""),
        # Case(40, 2188189693529, ""),
    ]
    for c in cases:
        actual, p = polymerize(template, pairs, c.steps)
        # assert p == c.p
        assert actual == c.expected, "Case: {}".format(c)


def test_polymerize():
    template, pairs = getPolymer(getInput())
    actual, _ = polymerize(template, pairs, 10)
    assert actual == 2768


def test_ddlist():
    l = DoubleLinkedList()
    l.prepend(1)
    l.prepend(2)
    l.prepend(3)
    expected = [3, 2, 1]

    assert l.toList() == expected
    assert l.toListRev() == list(reversed(expected))


def test_ddlist():
    l = DoubleLinkedList([1, 2, 3])

    expected = [1, 2, 3]
    assert l.toList() == expected
    assert l.toListRev() == list(reversed(expected))


def test_ddlist_iter():
    l = DoubleLinkedList()
    l.prepend(1)
    l.prepend(2)
    l.prepend(3)
    iterator = iter(l)
    actual = [n.data for n in iterator]
    expected = [3, 2, 1]

    assert actual == expected


def test_ddlist_insert_after():
    l = DoubleLinkedList()
    l.prepend(1)
    l.prepend(2)
    l.prepend(3)
    iterator = iter(l)
    first = next(iterator)
    l.insert_after(first, 4)

    actual = l.toList()
    expected = [3, 4, 2, 1]
    assert actual == expected


def test_ddlist_insert_after2():
    l = DoubleLinkedList()
    l.prepend(1)
    l.prepend(2)
    l.prepend(3)
    iterator = iter(l)
    next(iterator)
    next(iterator)
    last = next(iterator)
    l.insert_after(last, 4)

    actual = l.toList()
    expected = [3, 2, 1, 4]
    assert actual == expected
