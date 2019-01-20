from utils import Integers
from day9 import solve1, input9


test_input = """10 players; last marble is worth 1618 points: high score is 8317
13 players; last marble is worth 7999 points: high score is 146373
17 players; last marble is worth 1104 points: high score is 2764
21 players; last marble is worth 6111 points: high score is 54718
30 players; last marble is worth 5807 points: high score is 37305
"""


class TestDay9():
    def test_sample_inputs(self):
        lines = test_input.splitlines()
        test_cases = [Integers(line) for line in lines]
        for case in test_cases:
            nplayers, nmarbles, expected = case
            result = solve1(nplayers, nmarbles)
            assert result == expected

    def test_part1(self):
        nplayers, nmarbles = Integers(input9)
        expected = 424639
        result = solve1(nplayers, nmarbles)

        assert result == expected

    def test_part2(self):
        pass
