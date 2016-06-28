# Python实现支持向量机
使用Python实现支持向量机，代码思路来源于[机器学习实战](https://github.com/pbharrin/machinelearninginaction)。

# 线性可分支持向量机
构建分类器,寻找一个超平面(hyperplane), 使得距离分割超平面最近的点和分割超平面的间隔(margin)尽可能远。使分类器尽可能健壮。支持向量(support vector)就是离分割超平面最近的那些点。
分割超平面的对应方程为**w****x**+b=0, 它由法向量**w**和截距b决定。点到超平面的距离为|**w****A**+b|/||**w**||。**w****x**表示**w**和**x**的内积。

计算数据点到分割面距离并确定分割面的放置位置, 间隔:label * (**w****x**+b)。label=1或-1。

最小间隔最大化:

![equation](https://latex.codecogs.com/gif.latex?%5Carg%20%5C%20%5Cmax_%7Bw%2Cb%7D%20%5C%7B%5Cmin_%7Bn%7D%5C%28label*%28%5Cmathit%7B%5Cmathbf%7Bw%5ETx%7D%7D&plus;b%29%29*%5Cfrac%7B1%7D%7B%7C%7C%5Cmathbf%7Bw%7D%7C%7C%7D%29%5C%7D)