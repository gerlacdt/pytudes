import day7
import myutils
import unittest


class TestDay7(unittest.TestCase):
    def test_tree(self):
        input1 = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''

        result = day7.findRoot(input1)
        expected = ('tknk', '41', ['ugml', 'padx', 'fwft'])

        self.assertEqual(result, expected)

    def test_tree_input(self):
        input1 = myutils.readFile('./data/input7.txt')
        result = day7.findRoot(input1)
        expected = ('uownj', '12', ['wqdviv', 'ctmydr', 'pxdnb', 'qipooo', 'aazgvmc', 'eidmwnu'])

        self.assertEqual(result, expected)

    def test_norvig_tree_input(self):
        input1 = myutils.readFile('./data/input7.txt')
        result = day7.norvig_root(input1)
        expected = {'uownj'}

        self.assertEqual(result, expected)


    def test_norvig_tree_input(self):
        input1 = myutils.readFile('./data/input7.txt')
        result = day7.norvig_part2(input1)
        expected = 596

        self.assertEqual(result, expected)
