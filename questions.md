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
利用上述快速傅里叶变换（FFT）算法，实现一个详细的正则匹配过程：  
假设有一个主串 $S$（长度为 $n$）和一个模式串 $P$（长度为 $m$，只包含字母和通配符 ?，其中 ? 可以匹配任意单个字符）。请用 FFT 算法实现 $P$ 在 $S$ 中的所有匹配位置的查找
（3 分）

请给出该算法和时间复杂度分析（应为 $O(n \log n)$）。(默认n>>m)

##### 3 
给出一下对于这个的优化想法(依然用fast fourier transformation)

### 题目3 
对于这个包里面的结构优化一下(只用重构后端的结构)，然后push到自己的GitHub(可做不止一个commit, 最后结果应该是在自己的repository 内的branch 1)
（3分）
### 题目4 
#### 在里面实现以下逻辑
- 让user 之间加好友，删好友，让user可以直接看到他的好友列表以及这个用户列表
- 创建 admin， 可以看到别的所有的user， 批量注册用户，（可以用填表来实现，或者读csv来实现），同时还可以处理用户之间的加好友(强制性加好友)
- 这些放在branch 2里面(可以不止一次commit)
- 用sql来实现数据的存储

# 上交要求
- 给github 链接

- 算法题用pdf(latex来写)或者用markdown来写(放在github里面)

- 代码要写更新readme，写好gitignore
