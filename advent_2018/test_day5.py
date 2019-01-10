from day5 import part1, DoubleLinkedList


class TestDay5():
    def test_double_linked_list(self):
        myrange = 5
        expected = [i for i in range(myrange)]
        lst = DoubleLinkedList(expected)

        assert lst.to_list() == expected
        assert lst.to_list_reverse() == list(reversed(expected))

        for i in range(myrange):
            lst.delete(lst.search(i))

            expected.remove(i)
            assert lst.to_list() == expected



    def test_part1(self):
        pass
