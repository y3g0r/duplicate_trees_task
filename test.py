import unittest
from collections import deque


from tree import TreeNode
from tree import bft
from tree import print_tree

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


if __name__ == '__main__':
    unittest.main()
