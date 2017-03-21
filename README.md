# duplicate_trees_task

To visualize tree in demo
go [here](http://cpettitt.github.io/project/dagre-d3/latest/demo/interactive-demo.html?graph=%2F*%20Example%20*%2F%0Adigraph%20%7B%0A%20%20%20%20%2F*%20Note%3A%20HTML%20labels%20do%20not%20work%20in%20IE%2C%20which%20lacks%20support%20for%20%3CforeignObject%3E%20tags.%20*%2F%0A%20%20%20%20node%20%5Brx%3D5%20ry%3D5%20labelStyle%3D%22font%3A%20300%2014px%20%27Helvetica%20Neue%27%2C%20Helvetica%22%5D%0A%20%20%20%20edge%20%5BlabelStyle%3D%22font%3A%20300%2014px%20%27Helvetica%20Neue%27%2C%20Helvetica%22%5D%0A%20%20%20%201%20%20%5Blabel%3D%22A%20%3A%201%20%22%5D%3B%0A%20%20%20%202%20%20%5Blabel%3D%22X%20%3A%202%20%22%5D%3B%0A%20%20%20%203%20%20%5Blabel%3D%22H%20%3A%203%20%22%5D%3B%0A%20%20%20%204%20%20%5Blabel%3D%22G%20%3A%204%20%22%20style%3D%22fill%3A%20%23ed7979%22%5D%3B%0A%20%20%20%205%20%20%5Blabel%3D%22E%20%3A%205%20%22%20style%3D%22fill%3A%20%23b7e0e8%22%5D%3B%0A%20%20%20%206%20%20%5Blabel%3D%22G%20%3A%206%20%22%20style%3D%22fill%3A%20%23ed7979%22%5D%3B%0A%20%20%20%207%20%20%5Blabel%3D%22E%20%3A%207%20%22%5D%3B%0A%20%20%20%208%20%20%5Blabel%3D%22H%20%3A%208%20%22%20style%3D%22fill%3A%20%23e9ed79%22%5D%3B%0A%20%20%20%209%20%20%5Blabel%3D%22A%20%3A%209%20%22%20style%3D%22fill%3A%20%23bba8a7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2010%20%5Blabel%3D%22B%20%3A%2010%22%20style%3D%22fill%3A%20%23bbb8b7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2011%20%5Blabel%3D%22C%20%3A%2011%22%20style%3D%22fill%3A%20%23bbc8c7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2012%20%5Blabel%3D%22H%20%3A%2012%22%20style%3D%22fill%3A%20%23e9ed79%22%5D%3B%0A%20%20%20%2013%20%5Blabel%3D%22A%20%3A%2013%22%20style%3D%22fill%3A%20%23bba8a7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2014%20%5Blabel%3D%22C%20%3A%2014%22%20style%3D%22fill%3A%20%23bbc8c7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2015%20%5Blabel%3D%22B%20%3A%2015%22%20style%3D%22fill%3A%20%23bbb8b7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2016%20%5Blabel%3D%22E%20%3A%2016%22%20style%3D%22fill%3A%20%23b7e0e8%22%5D%3B%0A%20%20%20%2017%20%5Blabel%3D%22E%20%3A%2017%22%20style%3D%22fill%3A%20%23e8b7e8%22%5D%3B%0A%20%20%20%2018%20%5Blabel%3D%22E%20%3A%2018%22%20style%3D%22fill%3A%20%23b7e0e8%22%5D%3B%0A%20%20%20%2019%20%5Blabel%3D%22E%20%3A%2019%22%20style%3D%22fill%3A%20%23e8b7e8%22%5D%3B%0A%20%20%20%2020%20%5Blabel%3D%22A%20%3A%2020%22%20style%3D%22fill%3A%20%23bba8a7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2021%20%5Blabel%3D%22B%20%3A%2021%22%20style%3D%22fill%3A%20%23bbb8b7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2022%20%5Blabel%3D%22C%20%3A%2022%22%20style%3D%22fill%3A%20%23bbc8c7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2023%20%5Blabel%3D%22A%20%3A%2023%22%20style%3D%22fill%3A%20%23bba8a7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2024%20%5Blabel%3D%22B%20%3A%2024%22%20style%3D%22fill%3A%20%23bbb8b7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2025%20%5Blabel%3D%22C%20%3A%2025%22%20style%3D%22fill%3A%20%23bbc8c7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2026%20%5Blabel%3D%22D%20%3A%2026%22%20style%3D%22fill%3A%20%23bbd8d7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2027%20%5Blabel%3D%22A%20%3A%2027%22%20style%3D%22fill%3A%20%23bba8a7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2028%20%5Blabel%3D%22B%20%3A%2028%22%20style%3D%22fill%3A%20%23bbb8b7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2029%20%5Blabel%3D%22C%20%3A%2029%22%20style%3D%22fill%3A%20%23bbc8c7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2030%20%5Blabel%3D%22A%20%3A%2030%22%20style%3D%22fill%3A%20%23bba8a7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2031%20%5Blabel%3D%22B%20%3A%2031%22%20style%3D%22fill%3A%20%23bbb8b7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2032%20%5Blabel%3D%22C%20%3A%2032%22%20style%3D%22fill%3A%20%23bbc8c7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%2033%20%5Blabel%3D%22D%20%3A%2033%22%20style%3D%22fill%3A%20%23bbd8d7%22%5D%3B%20%2F*leaf*%2F%0A%20%20%20%201%20-%3E%202%3B%0A%20%20%20%201%20-%3E%203%3B%0A%20%20%20%201%20-%3E%204%3B%0A%20%20%20%203%20-%3E%205%3B%0A%20%20%20%203%20-%3E%206%3B%0A%20%20%20%203%20-%3E%207%3B%0A%20%20%20%204%20-%3E%208%3B%0A%20%20%20%205%20-%3E%209%3B%0A%20%20%20%205%20-%3E%2010%3B%0A%20%20%20%205%20-%3E%2011%3B%0A%20%20%20%206%20-%3E%2012%3B%0A%20%20%20%207%20-%3E%2013%3B%0A%20%20%20%207%20-%3E%2014%3B%0A%20%20%20%207%20-%3E%2015%3B%0A%20%20%20%208%20-%3E%2016%3B%0A%20%20%20%208%20-%3E%2017%3B%0A%20%20%20%2012%20-%3E%2018%3B%0A%20%20%20%2012%20-%3E%2019%3B%0A%20%20%20%2016%20-%3E%2020%3B%0A%20%20%20%2016%20-%3E%2021%3B%0A%20%20%20%2016%20-%3E%2022%3B%0A%20%20%20%2017%20-%3E%2023%3B%0A%20%20%20%2017%20-%3E%2024%3B%0A%20%20%20%2017%20-%3E%2025%3B%0A%20%20%20%2017%20-%3E%2026%3B%0A%20%20%20%2018%20-%3E%2027%3B%0A%20%20%20%2018%20-%3E%2028%3B%0A%20%20%20%2018%20-%3E%2029%3B%0A%20%20%20%2019%20-%3E%2030%3B%0A%20%20%20%2019%20-%3E%2031%3B%0A%20%20%20%2019%20-%3E%2032%3B%0A%20%20%20%2019%20-%3E%2033%3B%0A%7D%0A%0A)

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
