---
title: 染色
message: dsfz NOI篇 的密码
tags:
  - accnoi
  - 计数
date: 2024-11-14 18:27:33
---
### [染色](http://47.92.197.167:5283/contest/553/problem/2)

题目简述：给你一个序列 $c$，$c_i$ 表示 $i$ 的颜色。有两种操作 $c_{i-1}=c_i$，$c_{i+1}=c_i$。问在模 $2$ 意义下，所有可操作到的序列的个数。

- 我觉得这太好了，首先把原序列相同的颜色，缩起来，形如 $[1,1,1,2,2,2,1,1,1]\rightarrow [1,2,1]$。我们称这个操作为变换。那么原问题等价于，原序列经操作到达的新序列的变换，是原序列变换的子序列。这个不太回正，大概就是你可以覆盖，但是偏序关系不能乱。
- 接下来我们考虑对它计数。一种优秀的计数方式是，求原序列变换序列的子序列，满足子序列相邻元素颜色不同的数量。把长度为 $len$ 的那个数量记作 $f_i$。有 $ans=\sum_{i=1}^n\binom{n-1}{i-1}f_i$，其实可以看做一个区间，而我们算的是单点，自然就需要组合数计算一下，抻长到 $n$ 的组合数。
- 考虑 $f_i$ 的求解。由于要求相邻颜色不同所以直接在原序列上跑也是正确的。
- 设 $dp_{i,k,l}$ 表示第 $i$ 位之前结尾为颜色 $k$ 的，长度为 $l$ 的序列的方案数。$dp_{i,k,l}=dp_{i-1,k,l}+\sum dp_{i-1,\not=k,l-1}$。简单前缀和优化 $len_{i,j}$ 表示到第 $i$ 位之前，所有长度为 $j$ 的子序列的数量。有 $dp_{i,k,l}=dp_{i-1,k,l}+len_{i-1,l-1}-dp_{i-1,k,l-1}$。之后就是枚举长度，我们采取 $bitset$ 优化。$dp_{i,k}=dp_{i-1,k}+(len_{i-1}-dp_{i-1,k}<<1)$，之后维护 $len$ 就是简单的了。

```c++
#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10, M = 2e4 + 10;
int n, m, a[N],fac[N];
bitset<N> f[M], tmp;
int C(int x, int y) { return fac[x] == fac[y] + fac[x - y]; }
void solve(){
    cin>>n>>m;
    for (int i = 1; i <= n; i++) cin>>a[i];
    for (int i = 0; i <= m; i++) f[i].reset();
    f[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        int v = a[i];
        tmp = f[0] ^ f[v];
        f[v] = tmp << 1;
        f[0] = tmp ^ f[v];
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) ans ^= C(n - 1, i - 1) * f[0][i];
    cout<<ans;
}
int main() {
    freopen("color.in", "r", stdin);
    freopen("color.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    for (int i = 1; i < N; i++) {
        fac[i] = fac[i - 1];
        for (int v = i; v % 2 == 0; v /= 2) fac[i]++;
    }
    int T; cin>>T; while (T--) solve();
    return 0;
}

```

