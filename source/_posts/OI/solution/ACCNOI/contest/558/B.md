---
title: 统计
message: dsfz NOI篇 的密码
tags:
  - accnoi
  - 哈希
date: 2024-11-14 18:14:02
---
### [统计](http://47.92.197.167:5283/contest/558/problem/2)

- 题目简述：给一个序列 $a_i$，值域 $[1,m]$，称序列 $b$ 是好的，当且仅当 $\exist k,\forall i,k=\sum_{j=1}^n[b_j=i]$，就是序列每个数出现次数都相同，求原序列的所有子串中有多少个是好的。

- 题解：
- 考虑对原序列 $a$ 做替换，把相值域上邻两个数分别赋值为 $p$，$\frac{1}{p}$。那么只需要盘段区间乘积是否为 $1$，就可以判断相邻两个数是否数量相同。接着错开一位接着做之前的赋值。得到的权值一起考虑，就判断 $m$ 个数出现次数是都都相同。看代码，最好理解了。

```c++
#pragma GCC optimize(2)
#include <bits/stdc++.h>
using namespace std;
const int N = 1001000;
bitset<7368788> b; int s[N], top;
typedef long long ll;
const ll p = 998244353;
ll ksm(ll a, ll b)
{
    ll ans = 1;
    while (b)
    {
        if (b & 1)ans = ans * a % p;
        a = a * a % p; b >>= 1;
    }return ans;
}
ll inv(ll x) { return ksm(x, p - 2); }
ll c[N], d[N], x[N], y[N];
void init()
{
    for (int i = 2; i < 7368788; i++)
    {
        if (!b[i]) { s[++top] = i; }
        for (int j = 1; 1ll * s[j] * i < 7368788 && j <= top; j++)
        {
            b[s[j] * i] = true; if (i % s[j] == 0)break;
        }
    }
    d[1] = 1;
    for (int i = 500001; i <= 1000000; i++)s[i] = inv(s[i - 500000]);
    for (int i = 2; i <= 1000000; i += 2)c[i] = s[i >> 1], c[i - 1] = s[(i >> 1) + 500000];
    for (int i = 2; i <= 1000000; i += 2)d[i] = s[i >> 1], d[i + 1] = s[(i >> 1) + 500000];
}
void work()
{
    int n, m; io.read(n), io.read(m); x[0] = y[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        int col; io.read(col);
        if (col % 2 == 1 && col == m)x[i] = 1; else x[i] = c[col];
        if (col % 2 == 0 && col == m)y[i] = 1; else y[i] = d[col];
        x[i] = x[i] * x[i - 1] % p; y[i] = y[i] * y[i - 1] % p;
    }
    if (m > n)return cout << "0" << '\n', void();
    for (int i = 0; i <= n; i++)x[i] = x[i] * 1000000000ll + y[i];
    ll ans = 0;
    sort(x, x + 1 + n);
    for (ll i = 0; i <= n; i++)
    {
        ll j = i;
        while (j + 1 <= n && x[j + 1] == x[i])j++;
        ans += (j - i + 1) * (j - i) / 2; i = j;
    }
    io.write(ans, '\n');
}
int main()
{
    freopen("st.in", "r", stdin); freopen("st.out", "w", stdout);
    init(); int T; io.read(T); while (T--) work(); return 0;
}

```