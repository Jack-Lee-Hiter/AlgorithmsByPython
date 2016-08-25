#!/bin/bash
:<<!EOF!
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
For example, assume that words.txt has the following content:

the day is sunny the the
the sunny is is

Your script should output the following, sorted by descending frequency:
the 4
is 3
sunny 2
day 1
Note:
!EOF!

awk '{for(i=1;i<=NF;i++) a[$i]++} END {for(k in a) print k,a[k]}' words.txt | sort -k2 -nr
:<<!EOF!
注释：
awk文本分析；NF的值是每行的总列数；--k2 表示按照第二列排序 -nr表示按照逆序排列
!EOF!
