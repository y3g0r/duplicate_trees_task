from tree import TreeNode, serialize
import sys

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

print(serialize(root, compare_values=bool(int(sys.argv[1])), minheight=int(sys.argv[2])))