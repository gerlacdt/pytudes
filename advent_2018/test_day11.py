from day11 import part1, part2, input11


class TestDay11():
    def test_part1(self):
        result = part1(input11)
        expected = (30, (20, 50))

        assert result == expected

    # def test_part2(self):
    #     result = part2(input11)
    #     expected = (30, (20, 50))

    #     assert result == expected
