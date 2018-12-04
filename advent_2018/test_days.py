import days


class TestAdvent(object):
    def test_day1_part1(self):
        result = days.day1_part1()
        expected = 459
        assert result == expected

    def test_day1_part2(self):
        result = days.day1_part2()
        expected = 65474
        assert result == expected

    def test_day2(self):
        result = days.day2_part1()
        expected = 9139
        assert result == expected

    def test_day2_part2(self):
        result = days.day2_part2()
        expected = "uqcidadzwtnhsljvxyobmkfyr"
        assert result == expected

    def test_day3(self):
        result1, result2 = days.day3_part12()
        expected1, expected2 = 113716, 742
        assert result1 == expected1
        assert result2 == expected2
