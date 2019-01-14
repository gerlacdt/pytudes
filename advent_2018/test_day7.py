from day7 import schedule, order, input7, getPairs, maxval
from utils import cat


class TestDay7():
    def test_part1(self):
        result = cat(order(getPairs(input7)))
        expected = "BCEFLDMQTXHZGKIASVJYORPUWN"

        assert result == expected

    def test_part2(self):
        result = maxval(schedule(getPairs(input7))) + 1
        expected = 987
        assert result == expected
