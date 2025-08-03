### 题目 1

设 $A$ 为一 $n \times n$ 矩阵。若 $A$ 的每一条从左上到右下的对角线（即所有满足 $i-j$ 相同的位置）上的元素都相等，则称 $A$ 为 **反向对称矩阵**。其形状可示意如下：

\[
\begin{pmatrix}
a_{n-1} & a_{n-2} & a_{n-3} & \cdots & a_{1} & a_{0} \\
a_{n}   & a_{n-1} & a_{n-2} & \cdots & a_{2} & a_{1} \\
\vdots  & \vdots  & \vdots  & \ddots & \vdots & \vdots \\
a_{2n-3}& \vdots  & \vdots  & \vdots & a_{n-1} & a_{n-2} \\
a_{2n-2}& a_{2n-3}& \vdots  & \vdots & a_{n}   & a_{n-1}
\end{pmatrix}
\]


**要求**


1. **算法设计**  
   设计一个算法：给定上述压缩表示以及一个长度为 $n$ 的向量 $v$，输出矩阵–向量乘积 $A \cdot v$。(pseudo code only)

2. **复杂度分析**  
   证明你的算法的运行时间上界。


### 题目2

##### 1
这个是 fast fourier transformation 的教程，不需要懂他的原理，只需要知道他的输入和输出是什么
https://youtu.be/iTMn0Kt18tg?si=0BWbQ9uM3x6usVty
##### 2
用以上算法实现一下正则匹配，并且给出复杂度

##### 3 
给出一下这个的复杂度