---
title: 岛屿
message: dsfz NOI篇 的密码
tags:
  - accnoi
  - 计数
date: 2024-11-14 18:12:04
---
### [岛屿](http://47.92.197.167:5283/contest/552/problem/1)

- 题目简述：有 $2N$ 个点，有两种颜色，其中有 $N$ 个红点，$N$ 个蓝点，原来图上有 $N$ 条边，分别是 $X$ 条红红边，$X$ 条蓝蓝边，$Y$ 条红蓝边，每个点只被一条边连着（$2X+Y=N$）。现在要再加 $N$ 条边使得，每个点恰好被一条新加边所连着，而且新连的边要保证两端分别为红色和蓝色，问最后连成的图的联通块期望。
- 首先这题的状态设计就**非常神奇**，$F(x,y)$ 表示有 $x$ 条红红边，$x$ 条蓝蓝边，$y$ 条红蓝边的期望联通块个数
  - 反正我是不知道如何对联通块个数已知的条件计数，后求期望
- 转移就更加神奇了。
  - 我原本用，当前所剩的所有边的点暴力量量配对算方案数，按概率转移，之后发现没有优化空间。
- 题解直接钦定转移顺序。如果有红蓝边先考虑红蓝边的贡献。直到没有红蓝边，之后再考虑是否可以使红红边与蓝蓝边拼一起形成新的红蓝边。
  - **考虑为什么是对的！** 这是因为，一个联通块必然是一个环，而一个环上若有非红蓝边，一定可以在没有红蓝边之后加入。若有红蓝边先考虑红蓝边必然会被加红蓝边所计算。

$$
F(x,y)=
\begin{cases}
F(x,y-1)+\frac{1}{2x+y}&y\not=0\\
F(x-1,y+1)&y=0
\end{cases}
$$

$$
F(x,y)=
\begin{cases}
F(x,y-1)+\frac{1}{2x+y}&y\not=0\\
F(x-1,1)=F(x-1,0)+\frac{1}{2x-1}&y=0
\end{cases}
$$

- $F(x,y)=$ $x$ 维度累加，后 $y$ 维度累计。即 $F(x,y)=F(0,0)+\sum_{i=1}^{x}\frac{1}{2i-1}+\sum_{j=1}^y\frac{1}{2x+j}$，其中 $F(0,0)$ 等于 $0$。

```c++
#include<bits/stdc++.h>
using namespace std;
#define lb long double
int x,y;
lb ans;
int main()
{
	freopen("island.in","r",stdin);
    freopen("island.out","w",stdout);
	cin>>x>>y;
	for(int i=1;i<=x;i++) ans+=(lb)(1.0/(i*2-1));
	for(int i=1;i<=y;i++) ans+=(lb)(1.0/(i+x*2));
    printf("%.9Lf\n",ans);
	return 0;
}

```