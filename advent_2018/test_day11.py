from day11 import part1, input11


class TestDay11():
    def test_part1(self):
        result = part1(input11)
        expected = (30, (20, 50))

        assert result == expected
