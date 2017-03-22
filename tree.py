import random
import textwrap
from collections import deque
from collections import defaultdict
from collections import namedtuple
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

    @property
    def height(self):
        heights = deque((0,))
        for child in self._children:
            heights.append(child.height)
        return 1 + max(heights)


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

Edge = namedtuple('Edge', ['parent', 'child'])


def bft(tree):
    q = deque()
    q.append(tree)
    while q:
        current = q.popleft()
        q.extend(current.children())
        yield current


def bft_edges(tree):
    q = deque()
    q.append(Edge(parent=None, child=tree))
    while q:
        edge = q.popleft()
        for child in edge.child.children():
            q.append(Edge(edge.child, child))
        yield edge


def print_tree(tree):
    def _print_tree(tree):
        if not len(list(tree.children())):
            return {tree.data: []}
        children = []
        for node in tree.children():
            children += [_print_tree(node)]
        return {tree.data: children}

    pprint(_print_tree(tree))


def serialize(tree, compare_values=False, minheight=3, html=True):
    general_template = textwrap.dedent("""
    digraph {{
        node [rx=5 ry=5 labelStyle="font: 300 14px 'Helvetica Neue', Helvetica"]
        edge [labelStyle="font: 300 14px 'Helvetica Neue', Helvetica"]

    {node_declarations}
    {node_relations}
    }}
    """)

    if html:
        node_declaration_template = \
            '\t{node.id} [label="{node.data} : {node.id}" style="fill: {node_color}"];'
    else:
        node_declaration_template = \
            '\t{node.id} [label="{node.data} : {node.id}" color="black" fillcolor="{node_color}" style="filled"];'

    node_relation_template = \
        '\t{edge.parent.id} -> {edge.child.id};'

    dups = tree.duplicates(compare_values=compare_values, minheight=minheight)
    color_of = defaultdict(lambda: '#ffffff')
    colors = {'#ffffff'}
    color = '#ffffff'

    for dup_set in dups:
        while color in colors:
            rgb = [random.randint(89, 209) for _ in range(3)]
            color = '#' + ''.join('{:02X}'.format(clr) for clr in rgb)
        colors.add(color)
        for node in dup_set:
            color_of[node] = color

    declarations = []
    relations = []

    for edge in bft_edges(tree):

        decl = node_declaration_template.format(
            node=edge.child,
            node_color=color_of[edge.child]
        )
        declarations.append(decl)
        if not edge.parent:
            continue

        rel = node_relation_template.format(edge=edge)
        relations.append(rel)

    final = general_template.format(
        node_declarations="\n".join(declarations),
        node_relations="\n".join(relations)
    )

    return final