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
