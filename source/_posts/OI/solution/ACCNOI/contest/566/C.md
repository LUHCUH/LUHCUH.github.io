---
title: 人口局 DBA（dba）
message: dsfz NOI篇 的密码
tags:
  - accnoi
date: 2024-11-14 18:47:27
---
### [人口局 DBA（dba）](http://47.92.197.167:5283/contest/566/problem/3)

- 题目简述：有一个 $n$ 位 $m$ 进制数 $x$，$S(x)$ 表示 $x$ 的各个数位之和，求存在多少 $y<x$ 的正整数满足 $S(y)=S(x)$
- $1<m\le 2000,1\le n\le 2000$
- 基本的我们有类似统计 数位dp 的思想，枚举 $y$ 有多少位和 $x$ 的前缀相同，剩下的所有位置的限制都形如 $0\le y_i< m$。
- 显然，我们不定方程计数。$\sum y_i=S(x),0\le y_i< m$
- 设 $G(a,b)$ 表示 $a$ 位，和为 $b$ 的 $m$ 进制数的个数方案数。
- 设 $F(a,b,t)$，$a,b$ 同上，钦定 $t$ 个数，$m\le y_i$，的方案数
- 设 $G(a,b,t)$，$a,b$ 同上，只有 $t$ 个数，$m\le y_i$，的方案数

$$
\begin{aligned}
G(a,b)&=G(a,b,0)\\
F(a,b,t)&=\binom{b-tm+a-1}{a-1}\\
F(a,b,s)&=\sum{s\le t}\binom{n-s}{t-s}G(a,b,t)\\
&=\sum_{t=0}^{a-s}\binom{a-s}{t}G(a,b,s+t)\\
G(a,b,s)&=\sum_{t=0}^{a-s}\binom{a-s}{t}(-1)^t\binom{b-(s+t)m+a-1}{a-1}\\
G(a,b)&=G(a,b,0)=\sum_{t=0}^a\binom{a}{t}(-1)^t\binom{b-tm+a-1}{a-1}
\end{aligned}
$$

- 现在直接做是 $O(n^2m)$ 的，接着我们尝试把枚举前边不变后，第一个变化的位置的贡献合并，集体如下
- 为了方便我们约定这里 $y_i \to i$，$n-i\to n$，$s-\sum\limits_{k=0}^{i-1}y_k\to s$

$$
\begin{aligned}
\sum_{k=0}^{y-1}G(n,s-k)&=\sum_{k=0}^{y-1}\sum_{t=0}^n\binom{n}{t}(-1)^t\binom{s-k-tm+n-1}{n-1}\\
&=\sum_{t=0}^n\binom{n}{t}(-1)^t(\sum_{k=0}^{y-1}\binom{s-k-tm+n-1}{n-1})\\
&=\sum_{t=0}^n\binom{n}{t}(-1)^t(\binom{s-tm+n}{n}-\binom{s-y-tm+n}{n})
\end{aligned}
$$

- 到这，就可以愉快的 [参考实现 $\text O(n^2)$](http://47.92.197.167:5283/submission/256347) 啦。
