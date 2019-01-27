from day11 import maxpower


class TestDay11():
    def test_part1(self):
        result = maxpower()
        expected = (30, (20, 50), 3)
        assert result == expected

    def test_part2(self):
        result = max(maxpower(width=w) for w in range(300))
        expected = (88, (238, 278), 9)
        assert result == expected
