from collections import deque
from collections import defaultdict
from pprint import pprint


class TreeNode:
    def __init__(self, data, id=None):
        self._data = data
        self._children = []
        self._id = id

    @property
    def id(self):
        return self._id or hash(self)

    @property
    def data(self):
        return self._data

    def _node_type_check(self, node):
        if not issubclass(type(node), TreeNode):
            raise TypeError('Childs should be of type TreeNode')

    def insert_child(self, index, node):
        self._node_type_check(node)
        self._children.insert(index, node)

    def add_child(self, node):
        self._node_type_check(node)
        self._children.append(node)

    def children(self):
        for child in self._children:
            yield child

    @property
    def children_count(self):
        return len(self._children)

    def __getitem__(self, index):
        if index < len(self._children):
            return self._children[index]
        raise IndexError("Current tree has only {} children."
                         "Tried to get {}'s".format(len(self._children), index))

    def __repr__(self):
        return 'TreeNode({!r}, id={!r})'.format(self.data, self.id)

    def equals(self, b, compare_values=False):
        """return True if trees are equal"""
        # TODO: Don't use recursion
        if self is b:
            return True
        if compare_values and self.data != b.data:
            return False
        res = True
        if self.children_count != b.children_count:
            return False
        for i in range(self.children_count):
            res &= self[i].equals(b[i], compare_values)
            if not res:
                break
        return res

    def groups(self):
        """return mapping tree_height -> tree_size -> [nodes]"""
        # TODO: Don't use recursion
        def _groups(tree, table):
            heights = [0]
            sizes = [0]
            for child in tree.children():
                h, s = _groups(child, table)
                heights.append(h)
                sizes.append(s)
            h = 1 + max(heights)
            s = 1 + sum(sizes)
            table[h][s].append(tree)
            return h, s

        table = defaultdict(lambda: defaultdict(deque))
        _groups(self, table)
        return table

    def duplicates(self, minheight=1, compare_values=False):
        table = self.groups()
        result = []
        # compare only subtrees of the same height
        # flat tree - 2 iterations (2 heights: 2 for root and 1 for leaf)
        # nested tree (list) - n iterations
        for height in table:
            if height < minheight:
                continue
            # within the set of same height subtrees
            # compare only those with the same size
            # flat tree - 1 iteration (one size per height)
            # nested tree (list) - 1 iter
            for size in table[height]:
                # for each element in the group of same h and s will populate
                # it's own set of duplicates
                # but declare here because of scope
                duplicates = None

                # before first iteration
                # flat tree - up to (n - 1) nodes per height per size (nodes in tree - root (1))
                # nested tree - 1 node per height per size (so, zero iterations)
                # worst case - all nodes in group are unique - n(n-1)/2 compares (n of combinations)
                # best case all nodes in group are equal - (n-1) compares
                while len(table[height][size]) > 1:
                    group = table[height][size]
                    nodes_not_equal_to_current = deque()

                    current = group.popleft()
                    duplicates = set()  # set of duplicates of current node
                    while group:
                        tree = group.popleft()
                        if current.equals(tree, compare_values):
                            duplicates.update((current, tree))
                        else:
                            nodes_not_equal_to_current.append(tree)
                    table[height][size] = nodes_not_equal_to_current
                    if duplicates:
                        result.append(duplicates)
        return result


def bft(tree):
    q = deque()
    q.append(tree)
    while q:
        current = q.popleft()
        q.extend(current.children())
        yield current


def print_tree(tree):
    def _print_tree(tree):
        if not len(list(tree.children())):
            return {tree.data: []}
        children = []
        for node in tree.children():
            children += [_print_tree(node)]
        return {tree.data: children}

    pprint(_print_tree(tree))

if __name__ == '__main__':
    counter = 1
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


