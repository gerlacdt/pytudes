from day12 import part1, part2


class TestDay12():
    def test_part1(self):
        result = part1()
        expected = 3798
        assert result == expected

    def test_part2(self):
        result = part2()
        expected = 3900000002212
        assert result == expected
