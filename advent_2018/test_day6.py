from day6 import part1, part2, input6


class TestDay6:
    def test_part1(self):
        result = part1(input6)
        expected = 4887
        assert result == expected

    def test_part2(self):
        result = part2(input6)
        expected = 34096
        assert result == expected
