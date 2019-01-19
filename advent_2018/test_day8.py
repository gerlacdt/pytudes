from day8 import solve1, input8


class TestDay8():
    def test_part1(self):
        result = solve1(input8)
        expected = 41555
        assert result == expected
