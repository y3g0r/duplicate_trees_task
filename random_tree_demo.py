import random
import string
import argparse
import time
import sys

from tree import TreeNode
from tree import serialize

parser = argparse.ArgumentParser(description='Demo tree generator')
parser.add_argument('n_nodes', metavar='N',
                    type=int,
                    help="number of nodes in generated tree")
parser.add_argument('-c','--compvals',
                    dest='compvals', action='store_const',
                    const=True, default=False,
                    help="compare values while colorizing tree")
parser.add_argument('--minh', dest='minheight',
                    action='store', type=int, default=1,
                    help="min height of tree to be compared, default 1")
parser.add_argument('--maxh', dest='maxheight',
                    action='store', type=int, default=0,
                    help="max height for each node (except root), default N")
parser.add_argument('--maxb', dest='maxbreadth',
                    action='store', type=int, default=0,
                    help="max number of childs for each node, default N")
parser.add_argument('--ent', dest='entropy',
                    action='store', type=int, default=5,
                    help="dataset size. Default dataset is ascii letters. "
                    "If expected dataset size is bigger then ascii letters set "
                    "then it is extended with D_{n} where n is int")
parser.add_argument('-v','--verbose', dest='verbose',
                    action='store_const', const=True, default=False,
                    help="print to stderr time required to serialize tree (tree generation step excluded)")

args = parser.parse_args()

compare_values = args.compvals
minheight = args.minheight
number_of_nodes = args.n_nodes
max_breadth = args.maxbreadth or args.n_nodes
max_height = args.maxheight or args.n_nodes
datasetsize = args.entropy
dataset = [letter for letter in string.ascii_letters[:datasetsize]]
if len(dataset) < datasetsize:
    diff = datasetsize - len(dataset)
    dataset += ["D_{}".format(i) for i in range(diff)]
nodes = list()


root = TreeNode(random.choice(dataset), 1)
nodes.append(root)

try:
    for i in range(1, number_of_nodes):
        parent = random.choice(nodes)
        while parent.height >= max_height:
            if parent is root:
                break
            nodes.remove(parent)
            parent = random.choice(nodes)

        data = random.choice(dataset)
        newnode = TreeNode(data, i+1)

        parent.add_child(newnode)
        if parent.children_count == max_breadth:
            nodes.remove(parent)
        nodes.append(newnode)
except IndexError:
    print("Can't satisfy requested number of nodes"
          "because of max height and max breadth constraints."
          "generated {} nodes".format(i))

start = time.time()
output = serialize(root, compare_values=compare_values, minheight=minheight)
end = time.time() - start
print(output)
print(end, file=sys.stderr)
