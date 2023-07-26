---
layout:     post
title:      "余数"
subtitle:   "如何计算大数的余数"
date:       2023-01-03 15:14:00
author:     "donlv1997"
header-style: text 
catalog: true
mathjax: true
tags:
    - 数学
---

## 乘法逆元

$k^{-1}$是$k$关于模$p$的乘法逆元的代数式可以记为:

$$
k \cdot k^{-1} \equiv 1 \pmod p
$$

换成余数的写法即为：

$$
\text{rem}(k \cdot k^{-1},p) = 1
$$

即存在唯一的整数$q$和$r$使$r = \text{rem}(k \cdot k^{-1},p) = k \cdot k^{-1} - q * p = 1$。其中$q$称为商，$r \in \lbrace 0,1,...,k \cdot k^{-1} - 1 \rbrace$ 为余数。


## 费马小定理

设$p$是一个质数且$k$不为$p$的倍数则：

$$
k^{p-1} \equiv 1 \pmod p
$$

根据费马小定理(证明略)可知$k^{p-2}$是$k$关于模$p$的乘法逆元。

## 如何求大数的余数

设$p$是一个质数且$ k \in \lbrace 1,2,...,p-1 \rbrace $，如果要利用费马小定理求$k$关于模$p$的乘法逆元，问题是如何计算下式：

$$rem(k^{p-2},p)$$


## p = 97，a = 6 为例 

下式中的$\equiv x$均为$\equiv x \pmod{97}$的简写

$$
\begin{align*}
6^2 &\equiv 36 \\
6^4 &\equiv (6^2)^2 \equiv rem(36^2,97) \equiv 35 \\
6^8 &\equiv (6^4)^2 \equiv rem(35^2,97) \equiv 61 \\
6^{16} &\equiv (6^8)^2 \equiv rem(61^2,97) \equiv 35 \\
6^{32} &\equiv (6^{16})^2 \equiv rem(35^2,97) \equiv 61 \\
6^{95}&\equiv6\cdot6^2\cdot6^4\cdot6^8\cdot6^{16}\cdot6^{32}\cdot6^{32} \\
&\equiv6\cdot36\cdot35\cdot61\cdot35\cdot61\cdot61
\equiv 81
\end{align*}
$$

因此可以得知6关于模97的最小正整数乘法逆元为81。

## gcd法(Pulverizer)求乘法逆元

根据乘法逆元的余数写法：

$$
\text{rem}(k \cdot k^{-1},p) = k \cdot k^{-1} - q * p = 1
$$

因为$97$是质数且$6$小于$97$，故$6$与$97$互质。因此$\gcd(97,6)=1$，即存在线性组合$s \cdot 97 + t \cdot 6 = 1$。观察上式可知线性组合中的$t$就是$6$关于模$97$的乘法逆元(即$t=k^{-1}$,$k=6$,$p=97$)，使用Pulverizer法求线性组合$\gcd(x,y)=s \cdot x + t \cdot y$的步骤如下：

$$
\begin{array}{ccrcl} 
x & y & \text{rem}(x,y) & = & x-q \cdot y \\ 
\hline 
97 & 6 & 1 & = & 97 - 16 \cdot 6 \\ 
6  & 1 & 0 &  & 
\end{array}
$$

从上表可知当$s=1,t=-16$时，线性组合$s \cdot 97 + t \cdot 6$等于$1$，如果要得到一个最小正整数的乘法逆元，需对该式稍作变换：

$$
\begin{align*}
1 \cdot 97 - 16 \cdot 6 &= 1 \\
1 \cdot 97 - 16 \cdot 6 + 97 \cdot 6 - 97 \cdot 6 &= 1 \\
(-5) \cdot 97 + 81 \cdot 6 &= 1
\end{align*}
$$

可以得到$0 < t < 97$范围的乘法逆元81。