from utils import Inputstr, letters

test_input = "dabAcCaCBAcCcaDA"  # expected result is 10 units


def react(c1, c2):
    if c1.lower() == c2.lower() and c1 != c2:
        return True
    return False


input5 = Inputstr(5)


class Node():
    def __init__(self, value, previous, succ):
        self.value = value
        self.previous = previous
        self.succ = succ

    def __str__(self):
        return "{}, ({})".format(
            self.value,  self.succ)


class DoubleLinkedList():
    def __init__(self, arr=[]):
        self.head = None
        self.tail = None
        for item in arr:
            self.append(item)

    def insert(self, value):
        if not self.head:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
            return
        node = Node(value, None, self.head)
        self.head.previous = node
        self.head = node

    def append(self, value):
        if not self.tail:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
            return
        node = Node(value, self.tail, None)
        self.tail.succ = node
        self.tail = node

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.succ
        return None

    def to_list(self):
        current = self.head
        lst = []
        while current:
            lst.append(current.value)
            current = current.succ
        return lst

    def to_list_reverse(self):
        current = self.head
        lst = []
        while current.succ:
            current = current.succ

        while current:
            lst.append(current.value)
            current = current.previous
        return lst

    def delete(self, node):
        if not node.previous and not node.succ:
            self.head = None
            self.tail = None
            return

        if not node.previous:
            node.succ.previous = None
            self.head = node.succ
            return None

        if not node.succ:
            node.previous.succ = None
            self.tail = node.previous
            return None
        node.previous.succ = node.succ
        node.succ.previous = node.previous

    def __str__(self):
        return str(self.head)


# def chain(arr):
#     arr2 = arr[:]
#     current = 1
#     previous = 0
#     while current < len(arr2):
#         if react(arr2[previous], arr2[current]):
#             arr2 = arr2[:previous] + arr2[current+1:]
#             previous -= 1
#             current -= 1
#         else:
#             previous += 1
#             current += 1
#     return len(arr2)


def chain(arr):
    lst = DoubleLinkedList(arr)
    current = lst.head.succ
    previous = lst.head
    while current:
        if react(previous.value, current.value):
            tmp_prev = previous
            previous = previous.previous
            current = current.succ
            # print("delete prev: {}, prev_succ: {}".format(tmp_prev.value, tmp_prev.succ.value))
            lst.delete(tmp_prev.succ)
            lst.delete(tmp_prev)
        else:
            previous, current = current, current.succ
        # print("".join(lst.to_list()))
    return len(lst.to_list())


def part1(content=test_input):
    return chain(list(content))


def part2(content=test_input):
    # remove all letter pairs from given input
    minimum = 9999999
    arr = list(content)
    for letter in letters:
        arr2 = []
        for c in arr:
            if c == letter or c == letter.upper():
                continue
            else:
                arr2.append(c)

        # run reaction chain
        result = chain(arr2)
        print("done for letter: {}".format(letter))
        if result < minimum:
            minimum = result

    return minimum
