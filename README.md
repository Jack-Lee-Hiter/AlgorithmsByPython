# 尝试用Python实现一些简单的算法和数据结构
之前的算法和数据结构基本都是用Swift写的，现在尝试用Python实现一些简单的算法和数据结构。

## update 20160704
准备加入[《剑指offer》](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B00L5LKMVU?ie=UTF8&*Version*=1&*entries*=0)的习题python实现,以及机器学习过程中的一些算法

## update 20160717
加入leetcode部分

~~## update 20160730~~
## update 20160814
整理

如果对你有帮助，请记得点击github工程上的star，^_^ 现在总结如下：

[数据结构markdown格式](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md)

[链表及常见操作](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Lists.py)

[平衡查找树AVL](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/AVL.py)

[三种方法检测变位词Anagram](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/AnagramDetection.py)

[构建堆](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/BinaryHeap.py)

[二分查找](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/BinarySearch.py)

[二叉查找树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/BinarySearchTree.py)

[二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/BinaryTree.py)

[冒泡排序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/BubbleSort.py)

[英语单词拼写检查算法](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/CheckErrorWord.py)

[几个小的动态规划问题](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Dynamic%20Programming.py)

[Hash及常见操作](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Hash.py)

[插入排序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/InsertionSort.py)

[归并排序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/MergeSort.py)

[解析树ParseTree](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/ParseTree.py)

[队列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Queue.py)

[快排](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/QuickSort.py)

[基数排序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/RadixSort.py)

[一些递归算法](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Recursion.py)

[选择排序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/SelectionSort.py)

[希尔排序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/ShellSort.py)

[栈及常见应用](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Stack.py)

[分治算法](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/divideAndConquer.py)

[堆排序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/heapSort.py)

[正则表达式和一个使用正则表达式的图片爬虫](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/tree/master/regularExpression)

[剑指offer](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/tree/master/Target%20Offer)

[面试题2：实现Singleton模式](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/Singleton.py)

[面试题3：二维数组中的查找](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E6%9F%A5%E6%89%BE.py)：对于在一个每一行从左到右依次递增，每一列从上到下依次递增的二维数组查找一个元素，可以选择从数组左上角开始查找array[i]\[j]，如果目标元素大于array[i]\[j]，i+=1，如果元素小于array[i]\[j]，j-=1，依次循环直至找到这个数。

[面试题4：替换空格](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.py)：如果直接每次遇到空格添加'%20'，那么空格后面的数字就需要频繁向后移动。遇到这种移动问题，我们可以尝试先给出最终需要的长度，然后从后向前扫描，同时给定两个指针来保证定位。**逆向思维**

[面试题5：从头到尾打印链表](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%8F%8D%E5%90%91%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.py)：从头到尾遍历链表，并用一个栈存储每个结点的值，之后出栈输出值即可。

[面试题6：重建二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91.py)：利用二叉树前序遍历和中序遍历的特性。前序遍历的第一个值一定为根节点，对应于中序遍历中间的一个点。在中序遍历序列中，这个点左侧的均为根的左子树，这个点右侧的均为根的右子树。这时可以利用递归，分别取前序遍历[1:i+1]和中序遍历的[:i]对应与左子树继续上一个过程，取前序遍历[i+1:]和中序遍历[i+1]对应于右子树继续上一个过程，最终得以重建二叉树。

[面试题7：用两个栈实现队列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E7%94%A8%E4%B8%A4%E4%B8%AA%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.py)：需要两个栈Stack1和Stack2，push的时候直接push进Stack1。pop需要判断Stack1和Stack2中元素的情况，Stack1空的话，直接从Stack2 pop，Stack1不空的话，把Stack1的元素push进入Stack2，然后pop Stack2的值。[推广：用两个队列实现栈](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E7%94%A8%E4%B8%A4%E4%B8%AA%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.py)

[面试题8：旋转数组的最小数字](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%B0%8F%E6%95%B0%E5%AD%97.py)：二分查找的变形，注意到旋转数组的首元素肯定不小于旋转数组的尾元素，设置中间点。如果中间点大于首元素，说明最小数字在后面一半，如果中间点小于尾元素，说明最小数字在前一半。依次循环。同时，当一次循环中首元素小于尾元素，说明最小值就是首元素。但是当首元素等于尾元素等于中间值，只能在这个区域顺序查找。

[面试题9：斐波那契数列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97.py)：如何不使用递归实现斐波那契数列，需要把前面两个数字存入在一个数组中。斐波那契数列的变形有很多，如青蛙跳台阶，一次跳一个或者两个；铺瓷砖问题。**变态青蛙跳**，每次至少跳一个，至多跳n个，一共有f(n)=2<sup>n-1</sup>种跳法。考察数学建模的能力。

[面试题10：二进制中1的个数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.py)：注意到每个**非零**整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0，那么二进制数中的1的个数就会减少一个，因此可以利用一个循环，使得 n = n&(n-1) ，计算经过几次运算减少到0，就是有几个1。注意：书中给了另外两种方法，分别是原始n左移一位和右移一位的方法，因为Python不会出现整数溢出的情况，这里就不再考虑着两种方法。扩展：判断一个数值是不是2得整数次方，如果是的话，这个数的二进制数中有且只有一个1，那么这个数n会有 n&(n-1) == 0。或者求两个整数m和n需要改变m二进制中的多少位才能得到n，可以先做 m^n 的异或运算，然后求这个数中有多少个1。

[面试题11：数值的整数次方](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E5%80%BC%E7%9A%84%E6%95%B4%E6%95%B0%E6%AC%A1%E6%96%B9.py)：如果采用常规解法，需要注意的地方:当指数为负数的时候；当底数为零且指数为负数的情况；在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内。如果采用递归解法，当n为偶数, a<sup>n</sup> = a<sup>n/2</sup> * a<sup>n/2</sup>，当n为奇数, a<sup>n</sup> = a<sup>(n-1)/2</sup> * a<sup>(n-1)/2</sup> * a，利用右移一位代替除2运算，利用 &1 判断是否为奇数。同时需要注意**递归终止条件**，exponent = 1的话，return base，exponent = -1的话，return 1.0/base。再次提醒！必须写成 1.0/base，否则 1/base，返回一个integer 0！

[面试题12：打印1到最大的n位数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%89%93%E5%8D%B01%E5%88%B0%E6%9C%80%E5%A4%A7%E7%9A%84n%E4%BD%8D%E6%95%B0.py)：该题的要点是注意输入的n位数是否会导致溢出，因此利用字符串模拟整数的加法。**注意**：在打印函数中，需要判断打印的数字是否是以0开头的，同时判断条件是 num[i] != "0"，不能写作 num[i] != 0，因为是使用str类型的，后面一种写法导致判断无法成功。

[面试题13：在O(1)时间删除链表结点](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%9C%A8O(1)%E6%97%B6%E9%97%B4%E5%86%85%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%BB%93%E7%82%B9.py)：当要删除的结点不是尾结点而且不是仅有一个结点的头结点，可以把该结点i的下一个结点j的内容复制到结点i，同时把i结点的next指向j结点的next，然后再删除结点j。如果要删除的链表为单结点链表且待删除的结点就是头结点，需要把头结点置为None，如果删除的结点为链表的尾结点，那么就需要顺序遍历链表，找到尾节点前面一个结点，然后将其next置空。

[面试题14：调整数组顺序使奇数位于偶数前面](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E8%B0%83%E6%95%B4%E6%95%B0%E7%BB%84%E9%A1%BA%E5%BA%8F%E4%BD%BF%E5%A5%87%E6%95%B0%E4%BD%8D%E4%BA%8E%E5%81%B6%E6%95%B0%E5%89%8D%E9%9D%A2.py)：注重函数的扩展性能。把函数中的判断条件写成一个判断条件的函数，方便与函数的扩展。对于奇数位于偶数前面的情况，类似于快排，在头和尾分别设置一个指针，头指针指向奇数则后移，尾指针指向偶数则前移。

[面试题15：链表中倒数第k个结点](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%92%E6%95%B0%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py)：代码的鲁棒性。需要注意：如果输入的链表为空；k大于链表的长度；k为0的情况。对于正常情况，设置两个指针分别指向头结点，第一个指针向前走**k-1步**，走到正数第k个结点，同时保持第二个指针不动，然后第一个指针和第二个指针每次同时前移一步，这样第一个指针指向尾结点的时候，第二个指针指向倒数第k个结点。判断尾结点的条件是 **pNode.next == None**。

[面试题16：递归以及非递归实现反转链表](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)：需要注意三个问题：输入的链表头指针为None或者整个链表只有一个结点时，反转后的链表出现断裂，返回的翻转之后的头节点不是原始链表的尾结点。因此需要引入一个翻转后的头结点，以及一个指向当前结点的指针，一个指向当前结点前一个结点的指针，一个指向当前结点后一个结点的指针，防止出现断裂。推广：递归实现反转链表

[面试题17：合并两个排序的链表](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.py)：要注意特殊输入，如果输入是空链表，不能崩溃。

[面试题18：树的子结构](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%A0%91%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84.py):多出需要判断指针是不是None，避免访问空指针而造成程序崩溃。

[面试题19：二叉树的镜像](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%95%9C%E5%83%8F.py)：需要判断输入的结点为空或者输入的结点没有子树的情况。

[面试题20：顺时针打印矩阵](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E9%A1%BA%E6%97%B6%E9%92%88%E6%89%93%E5%8D%B0%E7%9F%A9%E9%98%B5.py)：首先需要判断每一步开始是的坐标点是否满足小于行数的一半且小于列数的一半，在最后一圈中，可能出现仅能向右走一行，仅能向右走一行向下走一列，向右走一行向下走一列向左走一行，能走完整一圈，一共四种情况。其中只有能向左走一行必然发生，不必判断，剩余的都需要判断发生条件。

[面试题21：包含min函数的栈](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%8C%85%E5%90%ABmin%E5%87%BD%E6%95%B0%E7%9A%84%E6%A0%88.py)：引入两个栈，一个栈每次push实际的数字，另一个minStack，如果push的数字小于minStack栈顶的数字，push新的数字，繁殖，把栈顶的数字再压入一遍。

[面试题22：栈的压入、弹出序列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%A0%88%E7%9A%84%E5%8E%8B%E5%85%A5%E5%BC%B9%E5%87%BA%E5%BA%8F%E5%88%97.py)：建立一个辅助栈，把push序列的数字依次压入辅助栈，每次压入后，比较辅助栈的栈顶元素和pop序列的首元素是否相等，相等的话就推出pop序列的首元素和辅助栈的栈顶元素，若最后辅助栈为空，则push序列可以对应于pop序列。

[面试题23：从上往下打印二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BB%8E%E4%B8%8A%E5%BE%80%E4%B8%8B%E6%89%93%E5%8D%B0%E4%BA%8C%E5%8F%89%E6%A0%91.py)：引入一个队列即可。推广：有向图的广度优先遍历也是基于队列的。

[面试题24：二叉搜索树的后续遍历序列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E7%BB%AD%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97.py)：根据后续遍历的性质，尾元素必定是树的根，同时小于尾元素的值是左子树，大于尾元素的值为右子树，且序列前半部分均小于尾元素，后半部分均大于尾元素（如果同时存在左右子树的话），可以将序列划分左子树序列和右子树序列，然后递归比较师妹每一段均满足此性质。可以减少递归深度的办法：某段的元素个数如果<=3，则返回True；某整段的最小元素不小于尾元素或者整段的最大元素不大于尾元素，说明仅有左子树或者右子树，返回True。

[面试题25：二叉树中和为某一值的路径](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.py)：递归

[面试题26：复杂链表的复制](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%A4%8D%E6%9D%82%E9%93%BE%E8%A1%A8%E7%9A%84%E5%A4%8D%E5%88%B6.py)：注意链表结点进行复制的时候，不能简单地写作 pCloned = pNode，这样的话之后对pCloned的操作也会作用在pNode上面，导致操作循环往复。需要重新定一个pCloned = ListNode(0)，然后对结点的.val  .next   .random 进行设置。同时，在将复制的结点的random指向原始链表结点的random的next的时候，需要先判断一下，原始链表结点的next是否为None，不为None再指向。

[面试题27：二叉搜索树与双向链表](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.py):按照左右子树分治，递归实现。根的左边连接左子树的最右边结点，右边连接右子树的最左边结点。

[面试题28：字符串的排列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8E%92%E5%88%97%E5%92%8C%E7%BB%84%E5%90%88.py)：依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。[扩展：字符串的组合](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8E%92%E5%88%97%E5%92%8C%E7%BB%84%E5%90%88.py)

[面试题29：数组中出现次数超过一半的数字](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97.py)：两种思路。第一种思路，出现次数超过一半的数字，不管如何，必然这个数字位于数组中间的位置，因此可以采用类似于快排的划分的方法，找到位于数组中间的位置的数字，然后在顺序检索是否这个数字出现次数超过一半。第二种思路根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，因此可以最开始保存两个数值：数组中的一个数字以及它出现的次数，然后遍历，如果下一个数字等于这个数字，那么次数加一，如果不等，次数减一，当次数等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，直到进行到最后，**然后再验证最后留下的数字是否出现次数超过一半**，因为可能前面的次数依次抵消掉，最后一个数字就直接是保留下来的数字，但是出现次数不一定超过一半。

[面试题30：最小的k个数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%9C%80%E5%B0%8F%E7%9A%84k%E4%B8%AA%E6%95%B0.py)：两种方法。第一种方法是基于划分的方法，如果是查找第k个数字，第一次划分之后，划分的位置如果大于k，那么就在前面的子数组中进行继续划分，反之则在后面的子数组继续划分，时间复杂度O(n)；第二种方法是可以适用于**海量数据**的方法，该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，如果遍历到的元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。

[面试题31：连续子数组的最大和](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E8%BF%9E%E7%BB%AD%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%92%8C.py)：关键的问题在于成功分析整个过程。对于连续子数组，可以用一个数值来存储当前和，如果当前和小于零，那么在进行到下一个元素的时候，直接把当前和赋值为下一个元素，如果当前和大于零，则累加下一个元素，同时用一个maxNum存储最大值并随时更新。也可以利用动态规划解决。

[面试题32：从1到n整数中1出现的次数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B4%E6%95%B0%E4%B8%AD1%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0.py)：利用[数字规律](http://blog.csdn.net/u012505432/article/details/51889052)实现更为简单。

[面试题33：把数组排成最小数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0.py)：首先将数组中的数字全部转换为字符串存储在一个新的数组中，然后比较每两个数字串的拼接的mn和nm的大小，若mn<nm，则m更小，反之n更小，然后把更小的数放入一个新的List中，最后输出即可。使用冒泡排序很方便。

[面试题34：丑数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%B8%91%E6%95%B0.py)：空间换时间。建立一个长度为n的数组，保存这n个丑数。在进行运算的时候，某个位置需要求得丑数一定是前面某个丑数乘以2、3或者5的结果，我们分别记录之前乘以2后能得到的最大丑数M<sub>2</sub>，乘以3后能得到的最大丑数M<sub>3</sub>，乘以5后能得到的最大丑数M<sub>5</sub>，那么下一个丑数一定是M<sub>2</sub>，M<sub>3</sub>，M<sub>5</sub>中的最小的那一个。同时注意到，已有的丑数是按顺序存放在数组中的。对乘以2而言，肯定存在某一个丑数T<sub>2</sub>，排在他之前的每一个丑数乘以2得到的结果都会小于已有的最大丑数，在他之后的每一个丑数乘以2得到的结果都会太大，我们只需记下这个丑数的位置，每次生成新的丑数的时候，去更新这个T<sub>2</sub>。对于3和5同理。

[面试题35：第一个只出现一次的字符](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E5%AD%97%E7%AC%A6.py)：先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。再遍历一遍字符串，找到hash值等于1的输出即可。

[面试题36：数组中的逆序对](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%80%86%E5%BA%8F%E5%AF%B9.py)：这道题可以这么想，我们要找到数组中的逆序对，可以看做对数据进行排序，需要交换数组中的元素的次数，但是防止相同大小的元素发生交换，因此需要选择一个稳定的排序方法，记录发生交换的次数。那么，基于比较的稳定的排序方法中，最快的方法就是归并了，所以直接按照归并排序的思路，将数组分解、合并、排序即可。但是需要注意的是，在常规归并排序的时候，如果前一个元素大于后一个元素，直接进行交换即可，只进行了一次操作，但是对于这道题来讲，对于每一次的归并段，我们选择从后向前遍历，前面的归并段的某一个数值left[i]如果大于后面的某一个数值right[j]，因为在right自己独自排序的过程中，已经保证了right是有序的，所以j位置前面的数字全部小于right[j]，所以在这里逆序对的个数就会是 j-start-length，其中start是整个数组的起点，length是left的长度，然后再进行交换。

[面试题37：两个链表的第一个公共结点](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%85%AC%E5%85%B1%E7%BB%93%E7%82%B9.py)：首先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走m-n个结点，然后两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。

[面试题38：数字在排序数组中出现的次数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E5%AD%97%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0.py)：二分查找的扩展。可以构造两个函数。第一个函数查找目标数字出现的最前面的位置，先使用二分查找找到该数字，如果该数字的index > 0而且该数字前面一个数字等于k的话，那么就令end=middle-1，继续二分查找。对于第二个函数，查找目标数字出现的最后面的位置，反之编写。最后如果**数字存在**的话，令走后面的index减去最前面的index然后+1即可。**在进行有序数组的元素查找，可以先尝试一下二分查找**

[面试题39：二叉树的深度](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%B7%B1%E5%BA%A6.py)：利用递归实现。如果一棵树只有一个结点，那么它的深度为1。递归的时候无需判断左右子树是否存在，因为如果该节点为叶节点，它的左右子树不存在，那么在下一级递归的时候，直接return 0。同时，记得每次递归返回值的时候，深度加一操作。

[面试题39：判断平衡二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%88%A4%E6%96%AD%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.py)：基于二叉树的深度，再次进行递归。以此判断左子树的高度和右子树的高度差是否大于1，若是则不平衡，反之平衡。

[面试题40：数组中只出现一次的数字](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E6%95%B0%E5%AD%97.py)：**任何一个数字异或他自己都等于0**，**0异或任何一个数都等于那个数**。数组中出了两个数字之外，其他数字都出现两次，那么我们从头到尾依次异或数组中的每个数，那么出现两次的数字都在整个过程中被抵消掉，那两个不同的数字异或的值不为0，也就是说这两个数的异或值中至少某一位为1。我们找到结果数字中最右边为1的那一位i，然后一次遍历数组中的数字，如果数字的第i位为1，则数字分到第一组，数字的第i位不为1，则数字分到第二组。这样任何两个相同的数字就分到了一组，而两个不同的数字在第i位必然一个为1一个不为1而分到不同的组，然后再对两个组依次进行异或操作，最后每一组得到的结果对应的就是两个只出现一次的数字。

[面试题41：和为s的两个数字](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%92%8C%E4%B8%BAs%E7%9A%84%E4%B8%A4%E4%B8%AA%E6%95%B0%E5%AD%97.py)：设定两个指针，一个指向数组的起点，一个指向数组的终点，然后对两个数字求和，如果和大于目标值，则把后一个指针前移，如果和小于目标值，则把前一个指针后移。两个指针交汇的时候如果还没找到，就终止操作。

[面试题41：和为s的连续正数序列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%92%8C%E4%B8%BAs%E7%9A%84%E8%BF%9E%E7%BB%AD%E6%95%B4%E6%95%B0%E5%BA%8F%E5%88%97.py)：设定两个指针，先分别指向数字1和数字2，并设这两个指针为small和big，对small和big求和，如果和大于目标值，则从当前和中删除small值，并把small值加一，如果和小于目标值，则把big值加一，再把新的big值加入和中。如果和等于目标值，就输出small到big的序列，同时把big加一并加入和中，继续之前的操作。

[面试题42：翻转单词顺序](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E7%BF%BB%E8%BD%AC%E5%8D%95%E8%AF%8D%E9%A1%BA%E5%BA%8F.py)：首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后从前往后依次遍历新字符串，如果遇到空格，就把空格前的字符串用reverse翻转，添加空格，继续遍历。需要注意的是，如果新字符串结尾不是空格，当遍历到结尾的时候，前一个空格到结尾的字符串没有翻转，因此记得跳出遍历后，需要再完成一次翻转操作。

[面试题42：左旋转字符串](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%B7%A6%E6%97%8B%E8%BD%AC.py)：首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后根据题目中给出的左旋转字符串的个数n，用全字符串长度length减去旋转字符串个数n，求得对于新的字符串应该在哪一位进行旋转，然后分别旋转前[:length-n]子串和[length-n:]子串，重新拼接两个子串即可。

[面试题43：n个骰子的点数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/n%E4%B8%AA%E9%AA%B0%E5%AD%90%E7%9A%84%E7%82%B9%E6%95%B0.py)：用两个数组来存储骰子点数的每一个总数出现次数。在一次循环中，第一个数组中的第n个数字表示骰子和为n出现的次数。在下一次循环中加入一个新的骰子，此时和为n的骰子出现的次数应该等于上一次循环中骰子点数和为n-1，n-2，n-3，n-4，n-5，n-6的次数的总和，也就是把另一个数组的第n个数字对应上一个数组的n-1，n-2，n-3，n-4，n-5，n-6的次数的总和。同时需要注意的是，**每次使用新数组的时候，需要把数组所有位置清零**，因为我们对于第n位进行的累加操作，如果之前第n位有数字但不清零的话，会导致结果偏大。

[面试题44：扑克牌的顺子](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%89%91%E5%85%8B%E7%89%8C%E7%9A%84%E9%A1%BA%E5%AD%90.py)：先置换特殊字符AJQK为数字，排序，然后求出大小王即0的个数，然后求出除去0之外的，数组间的数字间隔(求间隔的时候记得减去1，比如4和5的间隔为5-4-1，表示4和5是连续的数字)，同时求间隔的时候需要鉴别是否出现对。最后比较0的个数和间隔的大小即可。

[面试题45：圆圈中剩下的数字](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E7%BA%A6%E7%91%9F%E5%A4%AB%E7%8E%AF.py)：递推公式：f[i] = (f[i-1]+m)%i。[详解](http://blog.csdn.net/u012505432/article/details/51747181)

[面试题46：求1+2+...+n](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%B1%82%E5%89%8Dn%E9%A1%B9%E5%92%8C.py)：利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。如果对n连续进行两次反运算，那么非零的n转换为True，0转换为False。利用这一特性终止递归。注意考虑测试用例为0的情况。

[面试题47：不用加减乘除做加法](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.py)：将两个数的加法看作两步，第一步是两个数相加但是不进位，第二步是记录之前的两数相加应该进位的地方加上前一个相加但是不进位的数。对于具体的两个不小于0的数m和n，第一步可以看做m和n的异或运算m^n，第二步可以看做m和n的与运算然后左移一位得到实际的进位位置(m&n)<<1。然后把两个得到的数字加起来继续操作，指到carry进位为0终止操作。对于含有负数的情况，见[博文](http://blog.csdn.net/u012505432/article/details/51902155)。

[面试题48：不能被继承的类(暂无)](https://github.com/Jack-Lee-Hiter)

[面试题49：把字符串转换成整数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%8A%8A%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2%E6%88%90%E6%95%B4%E6%95%B0.py)：主要是区分输入和合法性，比如输入一个None，输入一个空字符串 ""，或者输入的字符串中含有“+”或者“-”，或者输入的字符串中含有除去+ — 数字的非数字字符，如何段应正常的输出还是报错，需要考虑的全面一些。

[面试题50：树中两个节点的最低公共祖先](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E4%BD%8E%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)：首先来看比较简单的情况--[二叉搜索树的最低公共祖先](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E4%BD%8E%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)，对于二叉搜索树而言，每个节点的左子节点都小于这个数，右子节点都大于这个数，因此，我们比较当前节点和需要比较的结点m，n的大小，如果当前节点的值均大于m，n，则在当前节点的左子树继续操作，如果当前节点均小于m，n，则在当前节点的右子树继续操作，反之，则当前结点是最小公共祖先。而对于普通的二叉树而言，我们如果希望找到两个结点的最低公共祖先，那么我们可以先从树的根节点开始，找到根节点到结点m和结点n的路径，这时候我们就有两个List或者两个链表，然后就像前面题中遇到的寻找两个链表的公共结点一样，从后往前遍历两个List找到最靠后的第一个公共结点即可。

[面试题51：数组中重复的数字](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E7%BB%84%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E6%95%B0%E5%AD%97.py)：对于一个长度为n的数组里所有的数字都在0到n-1的范围内。查找重复数字的话，首先容易想到，对数组进行排序，然后遍历数组查找重复的数字，这样的时间复杂度为O(nlogn)；或者建立一个哈希表，这样实在O(n)的时间查找到，但是空间复杂度O(n)。另外一个空间复杂度为O(1)的算法如下，因为数字在0~n-1的范围内，那么如果数字没有重复，那么当数组排序之后数字i将出现在下标为i的位置，但是有重复的话，在某个位置j出现的数字将不是j。我们重排这个数组。从头到尾依次扫描这个数组中的每个数字，如果下标i不是出现数字i，那么就把数字i和i处的数字进行交换使数字i出现在应该出现的位置，如果新交换的数字还不是他应该出现的位置，继续交换，直至该处的数字m等于x下标m，如果在交换的过程中，第i处的位置数字等于第m处的数字，那么我们就找到了第一个重复的数字，记录这个数字，在从下一个位置继续扫描。

[面试题52：构建乘积数组](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84.py)：作图画出一个n*n的矩阵，即可看出规律。注意需要得到的向量初始化的时候，初始化的值应该为1。

[面试题53：正则表达式匹配](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%8C%B9%E9%85%8D.py)：这道题的关键在于缕清思路。具体情况分析看一下代码中的注释。

[面试题54：表示数值的字符串](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E8%A1%A8%E7%A4%BA%E6%95%B0%E5%80%BC%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2.py)：这道题的关键也在于讨论清楚情况，把所有可能出现的情况都考虑到。需要注意的是，指数E后面必须跟一个整数，不能没有数，也不能为小数。

[面试题55：字符流中第一个不重复的字符](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%AD%97%E7%AC%A6%E6%B5%81%E4%B8%AD%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%B8%8D%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%97%E7%AC%A6.py)：引入两个辅助存储空间。一个Dict存储当前出现的字符以及字符出现的次数，一个List存储当前出现字符。然后每次比较List的第一个字符在Dict中对应的次数，如果为1则输出这个字符，如果不为1则弹出这个字符比较下一个字符。

[面试题56：链表中环的入口结点](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%8E%AF%E7%9A%84%E5%85%A5%E5%8F%A3%E7%BB%93%E7%82%B9.py)：寻找链表中环的入口结点主要分成三个步骤：首先是设置两个快慢指针，如果快慢指针相遇，则快慢指针必然都在环中；然后从相遇的地方设置一个指针向后遍历并记录走的步数，当这个指针重新指到开始的位置的时候，当前对应的步数就是环中结点的数量k；然后设置两个指针从链表开始，第一个节点先走k步，然后第二个指针指到链表的开始，两个指针每次都向后走一步，两个指针相遇的位置就是链表的入口。

[面试题57：删除链表中重复的结点](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E7%BB%93%E7%82%B9.py)：我们需要设置一个指针preNode，preNode最开始为None，然后设置两个指针，pNode指向当前节点，pNext指向pNode下一个结点，⓵如果pNext不为空而且pNext的值等于pNode的值，那么就说明出现了重复数字的结点，就需要删除，然后从pNode开始遍历，如果结点值等于前面那个重复值，继续遍历。当遍历到None或者不同值结点的时候，这时候需要判断preNode结点，如果preNode结点为None，就说明我们刚才的重复结点是从整个链表的头结点开始重复的，就直接把pHead设置为当前结点，pNode也设置为当前结点。反之，如果preNode不为None，直接把preNode的下一个指针指向当前节点，pNode指向preNode即可；⓶如果pNext为空或者pNext的值不等于pNode的值，说明当前的这个pNode和后面的值不重复，直接令preNode = pNode，pNode指向下一个结点即可。

[面试题58：二叉树的下一个结点](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E7%BB%93%E7%82%B9.py)：三种情况：当前节点有右子树的话，当前节点的下一个结点是右子树中的最左子节点；当前节点无右子树但是是父节点的左子节点，下一个节点是当前结点的父节点；当前节点无右子树而且是父节点的右子节点，则一直向上遍历，直到找到最靠近的一个祖先节点pNode，pNode是其父节点的左子节点，那么输入节点的下一个结点就是pNode的父节点。

[面试题59：对称的二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%AF%B9%E7%A7%B0%E7%9A%84%E4%BA%8C%E5%8F%89%E6%A0%91.py)：分为递归和非递归的两种方式，思想是一样的。主要就是把叶子节点的None节点也加入到遍历当中。按照前序遍历二叉树，存入一个序列中。然后按照和前序遍历对应的先父节点，然后右子节点，最后左子节点遍历二叉树，存入一个序列。如果前后两个序列相等，那么说明二叉树是对称的。

[面试题60：把二叉树打印成多行](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%A0%91%E6%89%93%E5%8D%B0%E6%88%90%E5%A4%9A%E8%A1%8C.py)：引入两个队列。首先把当前层的节点存入到一个队列queue1中，然后遍历当前队列queue1，在遍历的过程中，如果节点有左子树或右子树，依次存入另一个队列queue2。然后遍历队列queue2，如此往复。

[面试题61：按之字形顺序打印二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%8C%89%E4%B9%8B%E5%AD%97%E5%BD%A2%E9%A1%BA%E5%BA%8F%E6%89%93%E5%8D%B0%E4%BA%8C%E5%8F%89%E6%A0%91.py)：按之字形顺序打印二叉树需要两个栈。我们在打印某一行节点时，拔下一层的子节点保存到相应的栈里。如果当前打印的奇数层，则先保存左子节点再保存右子节点到第一个栈里；如果当前打印的是偶数层，则先保存右子节点再保存左子节点到第二个栈里。

[面试题62：序列化二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%BA%8F%E5%88%97%E5%8C%96%E4%BA%8C%E5%8F%89%E6%A0%91.py)：最终要实现的是二叉树的序列化和反序列化。首先来看二叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出节点，再碰到左子节点或者右子节点为None的时候输出一个特殊字符"#"。对于反序列化，就是针对输入的一个序列构建一棵二叉树，我们可以设置一个指针先指向序列的最开始，然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继续转化为左子树和右子树。当遇到当前指向的字符为特殊字符"#"或者指针超出了序列的长度，则返回None，指针后移，继续遍历。

[面试题63：二叉搜索树的第k个结点](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py)：中序遍历输出一个序列，然后找到序列中第k个数即可。

[面试题64：数据流中的中位数](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%95%B0%E6%8D%AE%E6%B5%81%E4%B8%AD%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.py)：构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数。当目前两堆总数为偶数的时候，把数字存入最大堆，然后重排最大堆，如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；如果当前两堆总数为技术的时候，把数字存入最小堆，重排最小堆，如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数。

[面试题65：滑动窗口的最大值](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E7%9A%84%E6%9C%80%E5%A4%A7%E5%80%BC.py)：我们把可能成为滑动窗口的最大值的数值下标存入一个两端开口的队列index中。首先遍历输入数组，在遍历次数小于窗口长度的时候，如果index数组里面含有元素而且元素后面的下标值对应的输入数组的数如果小于当前遍历到的输入数组元素值，那么就把尾部的元素下标值不断pop出来，再压入当前输入元素对应的下标值。然后再从等于滑动窗口大小的位置继续遍历输入数组。首先把index数组的头元素下标值对应输入数组值压入输出数组。同样的，如果index数组里面含有元素而且元素后面的下标值对应的输入数组的数如果小于当前遍历到的输入数组元素值，那么就把尾部的元素下标值不断pop出来，同时，如果index数组内有元素，而且当一个数字的下标与当前处理的数字的下标只差大于或等于滑动窗口的大小时，这个数字已经从窗口中画出，可以从队列中删除了，再压入当前输入元素对应的下标值。**最后还需要在输出数组中append一下index手元素下标对应的输入元素值**。

[面试题66：矩阵中的路径](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E7%9F%A9%E9%98%B5%E4%B8%AD%E7%9A%84%E8%B7%AF%E5%BE%84.py)：回溯法。任选一个格子作为路径的起点。假设矩阵中某个格子的字符为ch并且这个格子将对应于路径上的第i个字符。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子外，其他各自都有4个相邻的格子。重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。

[面试题67：机器人的运动范围](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%9C%BA%E5%99%A8%E4%BA%BA%E7%9A%84%E8%BF%90%E5%8A%A8%E8%8C%83%E5%9B%B4.py)：回溯法。类似于面试题66。把方格看成一个m*n的矩阵，从（0，0）开始移动。当准备进入坐标(i, j)是，通过检查坐标的数位来判断机器人能否进入。如果能进入的话，接着判断四个相邻的格子。

[面试题补充：三元组实现稀疏矩阵相乘](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/multiSparse.py)

[面试题补充：稀疏矩阵的转置](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/transSparseMatrix.py)

[面试题补充：二叉搜索树的后续遍历](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E7%BB%AD%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97.py)

[面试题补充：八皇后问题](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%85%AB%E7%9A%87%E5%90%8E%E9%97%AE%E9%A2%98.py)

[面试题补充：分治法解决最近对问题](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%88%86%E6%B2%BB%E6%B3%95%E8%A7%A3%E5%86%B3%E6%9C%80%E8%BF%91%E5%AF%B9%E9%97%AE%E9%A2%98.py)

[面试题补充：判断平衡二叉树](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%88%A4%E6%96%AD%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.py)

[面试题补充：带锁的门](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E5%B8%A6%E9%94%81%E7%9A%84%E9%97%A8.py)

[面试题补充：格雷码](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%A0%BC%E9%9B%B7%E7%A0%81.py)

[面试题补充：正方体对面和相同](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%AD%A3%E6%96%B9%E4%BD%93%E5%AF%B9%E9%9D%A2%E5%92%8C%E7%9B%B8%E5%90%8C.py)

[面试题补充：转换字符串格式](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E8%BD%AC%E6%8D%A2%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A0%BC%E5%BC%8F.py)

[面试题补充：输出连续质数序列](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E8%BE%93%E5%87%BA%E8%BF%9E%E7%BB%AD%E8%B4%A8%E6%95%B0%E5%BA%8F%E5%88%97.py)

[面试题补充：递归和非递归实现二叉搜索树的三种遍历](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E9%80%92%E5%BD%92%E5%92%8C%E9%9D%9E%E9%80%92%E5%BD%92%E5%AE%9E%E7%8E%B0%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E4%B8%89%E7%A7%8D%E9%81%8D%E5%8E%86.py)

[面试题补充：二叉树的宽度](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%A0%91%E7%9A%84%E5%AE%BD%E5%BA%A6.py)

[LeetCode](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/tree/master/leetcode)

[logistic回归](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/tree/master/Logistic%20regression)

[SVM](https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/tree/master/SVM)
