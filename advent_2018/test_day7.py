from day7 import order, input7
from utils import cat


class TestDay7():
    def test_part1(self):
        result = cat(order(input7))
        expected = "BCEFLDMQTXHZGKIASVJYORPUWN"

        assert result == expected
