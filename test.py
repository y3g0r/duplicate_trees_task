import unittest
from collections import deque
from pprint import pprint

from tree import TreeNode
from tree import bft
from tree import serialize

class TestTreeNode(unittest.TestCase):
    def setUp(self):
        self.root_data = 1
        self.root = TreeNode(self.root_data)

    def test_data_descriptor(self):
        self.assertEqual(self.root_data, self.root.data)

        with self.assertRaises(AttributeError):
            self.root.data = 2

    def test_insert_child(self):
        with self.assertRaises(TypeError):
            self.root.insert_child(2)

        with self.assertRaises(TypeError):
            self.root.insert_child(0, 2)

        with self.assertRaises(TypeError):
            self.root.insert_child(TreeNode(2))

        self.root.insert_child(0, TreeNode(2))
        self.root.insert_child(0, TreeNode(3))
        self.root.insert_child(10, TreeNode(10))

        self.assertEqual(3, self.root._children[0].data)
        self.assertEqual(2, self.root._children[1].data)
        self.assertEqual(10, self.root._children[2].data)

    def test_add_child(self):
        with self.assertRaises(TypeError):
            self.root.add_child(2)

        for i in range(2, 5):
            self.root.add_child(TreeNode(i))

        for i in range(2, 5):
            self.assertEqual(
                i,
                self.root._children[i-2].data
            )

    def test_children(self):
        itr = self.root.children()
        with self.assertRaises(StopIteration):
            next(itr)

        data = [2, 3, 4, 5]
        for i in data:
            self.root.add_child(TreeNode(i))

        itr = self.root.children()
        first = next(itr)
        self.assertTrue(issubclass(type(first), TreeNode))
        self.assertEquals(data[0], first.data)

        for i, node in enumerate(itr):
            self.assertEquals(data[i+1], node.data)

    def test_getitem(self):
        with self.assertRaises(IndexError):
            tmp = self.root[0]

        data = [2, 3, 4, 5]
        for i in data:
            self.root.add_child(TreeNode(i))

        first = self.root[0]
        self.assertTrue(issubclass(type(first), TreeNode))
        self.assertEquals(data[0], first.data)

        for i in range(1, len(data)):
            self.assertEquals(data[i], self.root[i].data)

    def test_duplicate(self):
        node_01 = TreeNode('A', 1)
        node_02 = TreeNode('X', 2)
        node_03 = TreeNode('H', 3)
        node_04 = TreeNode('G', 4)
        node_05 = TreeNode('E', 5)
        node_06 = TreeNode('G', 6)
        node_07 = TreeNode('E', 7)
        node_08 = TreeNode('H', 8)
        node_09 = TreeNode('A', 9)
        node_10 = TreeNode('B', 10)
        node_11 = TreeNode('C', 11)
        node_12 = TreeNode('H', 12)
        node_13 = TreeNode('A', 13)
        node_14 = TreeNode('C', 14)
        node_15 = TreeNode('B', 15)
        node_16 = TreeNode('E', 16)
        node_17 = TreeNode('E', 17)
        node_18 = TreeNode('E', 18)
        node_19 = TreeNode('E', 19)
        node_20 = TreeNode('A', 20)
        node_21 = TreeNode('B', 21)
        node_22 = TreeNode('C', 22)
        node_23 = TreeNode('A', 23)
        node_24 = TreeNode('B', 24)
        node_25 = TreeNode('C', 25)
        node_26 = TreeNode('D', 26)
        node_27 = TreeNode('A', 27)
        node_28 = TreeNode('B', 28)
        node_29 = TreeNode('C', 29)
        node_30 = TreeNode('A', 30)
        node_31 = TreeNode('B', 31)
        node_32 = TreeNode('C', 32)
        node_33 = TreeNode('D', 33)
    
        node_01.add_child(node_02)
        node_01.add_child(node_03)
        node_01.add_child(node_04)
    
        node_03.add_child(node_05)
        node_03.add_child(node_06)
        node_03.add_child(node_07)
    
        node_04.add_child(node_08)
    
        node_05.add_child(node_09)
        node_05.add_child(node_10)
        node_05.add_child(node_11)
    
        node_06.add_child(node_12)
    
        node_07.add_child(node_13)
        node_07.add_child(node_14)
        node_07.add_child(node_15)
    
        node_08.add_child(node_16)
        node_08.add_child(node_17)
    
        node_12.add_child(node_18)
        node_12.add_child(node_19)
    
        node_16.add_child(node_20)
        node_16.add_child(node_21)
        node_16.add_child(node_22)
    
        node_17.add_child(node_23)
        node_17.add_child(node_24)
        node_17.add_child(node_25)
        node_17.add_child(node_26)
    
        node_18.add_child(node_27)
        node_18.add_child(node_28)
        node_18.add_child(node_29)
    
        node_19.add_child(node_30)
        node_19.add_child(node_31)
        node_19.add_child(node_32)
        node_19.add_child(node_33)
    
        root = node_01
    
        # Compare trees by structure and by values
    
        by_struct_and_value_group_01 = {
            # A leafs
            node_09, node_13, node_20, node_23, node_27, node_30
        }
        by_struct_and_value_group_02 = {
            # B leafs
            node_10, node_15, node_21, node_24, node_28, node_31
        }
        by_struct_and_value_group_03 = {
            # C leafs
            node_11, node_14, node_22, node_25, node_29, node_32
        }
        by_struct_and_value_group_04 = {
            # D leafs
            node_26, node_33
        }
        by_struct_and_value_group_05 = {
            # height 2 group 1
            node_05, node_18, node_16
        }
        by_struct_and_value_group_06 = {
            # height 2 group 2
            node_17, node_19
        }
    
        by_struct_and_value_group_07 = {
            # height 3
            node_08, node_12
        }
    
        by_struct_and_value_group_08 = {
            # height 4
            node_04, node_06
        }
    
        expected_duplicate_groups = [
            by_struct_and_value_group_01,
            by_struct_and_value_group_02,
            by_struct_and_value_group_03,
            by_struct_and_value_group_04,
            by_struct_and_value_group_05,
            by_struct_and_value_group_06,
            by_struct_and_value_group_07,
            by_struct_and_value_group_08,
        ]
    
        print("Expected:")
        pprint(expected_duplicate_groups)
    
        dup_groups = root.duplicates(minheight=1, compare_values=True)
        print("Actual:")
        pprint(dup_groups)
    
        assert len(dup_groups) == len(expected_duplicate_groups), \
            'Sizes of expected and actual groups are not equal'
    
        match = False
        for exp_set in expected_duplicate_groups:
            match = False
            for act_set in dup_groups:
                if exp_set ^ act_set == set():
                    match = True
                    break   # inner loop
            assert match, \
                "Expected group not found in result set. Expected: {}".format(exp_set)
    

def fill_children_flat(node, start=1, end=30):
    """Include start, don't include end"""
    for i in range(start, end):
        node.add_child(TreeNode(i))

def fill_children_binary(node, start=1, end=30):
    q = deque([node])

    for step, i in enumerate(range(start, end)):
        new = TreeNode(i)
        q.append(new)
        q[0].add_child(new)
        if step % 2 != 0:
            q.popleft()

def fill_children_deep(node, start=1, end=30):
    for i in range(start, end):
        new = TreeNode(i)
        node.add_child(new)
        node = new

class TestBreadthFirstTraversal(unittest.TestCase):

    def test_traverse_flat_tree(self):
        start = 0
        end = 30
        self.tree = TreeNode(start)
        fill_children_flat(self.tree, start=start+1, end=end)

        expected = ",".join(str(i) for i in range(30))
        actual = ",".join(str(node.data) for node in bft(self.tree))
        self.assertEqual(expected, actual)

    def test_traverse_bin_tree(self):
        start = 0
        end = 30
        self.tree = TreeNode(start)
        fill_children_binary(self.tree, start=start+1, end=end)

        expected = ",".join(str(i) for i in range(30))
        actual = ",".join(str(node.data) for node in bft(self.tree))
        self.assertEqual(expected, actual)

    def test_traverse_list_tree(self):
        start = 0
        end = 30
        self.tree = TreeNode(start)
        fill_children_binary(self.tree, start=start+1, end=end)

        expected = ",".join(str(i) for i in range(30))
        actual = ",".join(str(node.data) for node in bft(self.tree))
        self.assertEqual(expected, actual)

class TestSerialize(unittest.TestCase):
    def test_serialize(self):
        expect = """
digraph {{
    node [rx=5 ry=5 labelStyle="font: 300 14px 'Helvetica Neue', Helvetica"]
    edge [labelStyle="font: 300 14px 'Helvetica Neue', Helvetica"]
    {node_declarations}
    {node_relations}
}}
"""
        self.assertEqual(expect, serialize(None))


if __name__ == '__main__':
    unittest.main()
