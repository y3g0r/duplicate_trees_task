# duplicate_trees_task

To visualize tree in demo_client.py
go [here](http://cpettitt.github.io/project/dagre-d3/latest/demo/interactive-demo.html)

OR copy-paste this:
```
digraph {
    /* Note: HTML labels do not work in IE, which lacks support for <foreignObject> tags. */
    node [rx=5 ry=5 labelStyle="font: 300 14px 'Helvetica Neue', Helvetica"]
    edge [labelStyle="font: 300 14px 'Helvetica Neue', Helvetica"]
    1  [label="A : 1 "];
    2  [label="X : 2 "];
    3  [label="H : 3 "];
    4  [label="G : 4 " style="fill: #ed7979"];
    5  [label="E : 5 " style="fill: #b7e0e8"];
    6  [label="G : 6 " style="fill: #ed7979"];
    7  [label="E : 7 "];
    8  [label="H : 8 " style="fill: #e9ed79"];
    9  [label="A : 9 " style="fill: #bba8a7"]; /*leaf*/
    10 [label="B : 10" style="fill: #bbb8b7"]; /*leaf*/
    11 [label="C : 11" style="fill: #bbc8c7"]; /*leaf*/
    12 [label="H : 12" style="fill: #e9ed79"];
    13 [label="A : 13" style="fill: #bba8a7"]; /*leaf*/
    14 [label="C : 14" style="fill: #bbc8c7"]; /*leaf*/
    15 [label="B : 15" style="fill: #bbb8b7"]; /*leaf*/
    16 [label="E : 16" style="fill: #b7e0e8"];
    17 [label="E : 17" style="fill: #e8b7e8"];
    18 [label="E : 18" style="fill: #b7e0e8"];
    19 [label="E : 19" style="fill: #e8b7e8"];
    20 [label="A : 20" style="fill: #bba8a7"]; /*leaf*/
    21 [label="B : 21" style="fill: #bbb8b7"]; /*leaf*/
    22 [label="C : 22" style="fill: #bbc8c7"]; /*leaf*/
    23 [label="A : 23" style="fill: #bba8a7"]; /*leaf*/
    24 [label="B : 24" style="fill: #bbb8b7"]; /*leaf*/
    25 [label="C : 25" style="fill: #bbc8c7"]; /*leaf*/
    26 [label="D : 26" style="fill: #bbd8d7"]; /*leaf*/
    27 [label="A : 27" style="fill: #bba8a7"]; /*leaf*/
    28 [label="B : 28" style="fill: #bbb8b7"]; /*leaf*/
    29 [label="C : 29" style="fill: #bbc8c7"]; /*leaf*/
    30 [label="A : 30" style="fill: #bba8a7"]; /*leaf*/
    31 [label="B : 31" style="fill: #bbb8b7"]; /*leaf*/
    32 [label="C : 32" style="fill: #bbc8c7"]; /*leaf*/
    33 [label="D : 33" style="fill: #bbd8d7"]; /*leaf*/
    1 -> 2;
    1 -> 3;
    1 -> 4;
    3 -> 5;
    3 -> 6;
    3 -> 7;
    4 -> 8;
    5 -> 9;
    5 -> 10;
    5 -> 11;
    6 -> 12;
    7 -> 13;
    7 -> 14;
    7 -> 15;
    8 -> 16;
    8 -> 17;
    12 -> 18;
    12 -> 19;
    16 -> 20;
    16 -> 21;
    16 -> 22;
    17 -> 23;
    17 -> 24;
    17 -> 25;
    17 -> 26;
    18 -> 27;
    18 -> 28;
    18 -> 29;
    19 -> 30;
    19 -> 31;
    19 -> 32;
    19 -> 33;
}
```
Nodes with the same color are duplicates.

## Example invocations of random_tree_demo.py
```
$ python3 random_tree_demo.py 100 -h                      
usage: random_tree_demo.py [-h] [-c] [--minh MINHEIGHT] [--maxh MAXHEIGHT]
                           [--maxb MAXBREADTH] [--ent ENTROPY] [-v]
                           N

Demo tree generator

positional arguments:
  N                  number of nodes in generated tree

optional arguments:
  -h, --help         show this help message and exit
  -c, --compvals     compare values while colorizing tree
  --minh MINHEIGHT   min height of tree to be compared, default 1
  --maxh MAXHEIGHT   max height for each node (except root), default N
  --maxb MAXBREADTH  max number of childs for each node, default N
  --ent ENTROPY      dataset size. Default dataset is ascii letters. If
                     expected dataset size is bigger then ascii letters set
                     then it is extended with D_{n} where n is int
  -v, --verbose      print to stderr time required to serialize tree (tree
                     generation step excluded)

$ python3 random_tree_demo.py 100 -v | dot -Tps -o rendered/example1.ps
0.001222848892211914

$ python3 random_tree_demo.py 20 -v --compvals --ent 3 | dot -Tps -o rendered/example2.ps
0.0003457069396972656

$ python3 random_tree_demo.py 20 -v --compvals --ent 3 --minh 2 | dot -Tps -o rendered/example3.ps
0.0002856254577636719

# flat tree
$ python3 random_tree_demo.py 5 -v --compvals --ent 3 --minh 1 --maxh 1 | dot -Tps -o rendered/example4.ps
0.00023794174194335938

# bin tree
$ python3 random_tree_demo.py 15 -v --compvals --ent 3 --minh 2 --maxb 2 | dot -Tps -o rendered/example5.ps
0.00038051605224609375

# linked list
$ python3 random_tree_demo.py 5 -v --compvals --ent 3 --minh 2 --maxb 1 | dot -Tps -o rendered/example6.ps 
0.0001964569091796875
```
