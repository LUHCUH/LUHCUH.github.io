---
title: 乘法
message: dsfz NOI篇 的密码
tags:
  - accnoi
  - 数论
  - 折半搜索
date: 2024-11-14 18:34:37
---
### [乘法](http://47.92.197.167:5283/contest/554/problem/2)

- 题目简述：我们称 $k$ ($k\le 12$)进制下一个数是好的，当且仅当那个数个各个数位数字不同，给一个整数 $d$，求第二大的 $d$ 是 $d$ 的倍数的好的数。输出那个次大值的十进制数
- 题解：
- 注意到 $k\le 12$，啥意思，那个 $k$ 进制数最多有 $k$ 位，嘿嘿！，我咋没想到能，折半搜索
- 考虑对于只有 $6$ 个数的数字，暴力算，$O(\binom{12}{6}6!)$，不大，呱！
- 对于位数大于 $6$ 的数字，我们考虑由两部分拼接而成。分两部分 $O(\binom{12}{6})$
- 对于前 $6$ 位都要，对于后 $6$ 位可以只取其中小于 $6$ 位。此部分 $O(2\sum_{i=1}^6 i!)$
- 合起来，呱！$O(\binom{12}{6}(2\sum_{i=1}^6 i!))$，足以通过此题。

``` c++
#include <bits/stdc++.h>
using namespace std;
const int N = 2100, M = 12;
typedef long long ll;
struct node { ll m1, m2; node() { m1 = m2 = -1; }node(ll x, ll y) :m1(x), m2(y) {} };
void operator+=(node& x, ll y)
{
    if (x.m1 == y)return;
    if (x.m1 < y)x.m2 = x.m1, x.m1 = y;
    else x.m2 = max(x.m2, y);
}
ll n, k, nn, p[50], a[1 << M];
unordered_map<ll, node>mm;
int siz[1 << M]; node ans;
int lowbit(int x) { return x & (-x); }
void dfs1(ll num, int s, int x)
{
    if (x && num % n == 0)ans += num;
    if (s == 0) return mm[num % n] += num, void();
    for (int t = s; t; t ^= lowbit(t))
        dfs1(num + a[lowbit(t)] * p[x], s ^ lowbit(t), x + 1);
}
void dfs2(ll num, int s, int x)
{
    if (s == 0) return; int t = s;
    while (t)
    {
        const int id = lowbit(t);
        const ll m = num + a[id] * p[x];
        ll to = (n - m) % n; if (to < 0)to += n;
        if (mm.find(to) != mm.end())
        {
            auto& v = mm[to];
            if (v.m1 != -1) ans += v.m1 + m;
            if (v.m2 != -1) ans += v.m2 + m;
        }
        dfs2(m, s ^ id, x + 1); t ^= id;
    }
}
int main()
{
    freopen("multi.in", "r", stdin);
    freopen("multi.out", "w", stdout);
    cin >> n >> k; nn = 1 << k;
    p[0] = 1; siz[0] = 0;
    for (int i = 0; i < k; i++)a[1 << i] = i;
    for (int i = 1; i < nn; i++)siz[i] = siz[i >> 1] + (i & 1);
    for (int i = 1; i < 50; i++)p[i] = p[i - 1] * k;
    for (int s1 = 0; s1 < nn; s1++)if (siz[s1] == k / 2)
    {
        int s2 = nn - 1 - s1; mm.clear();
        dfs1(0, s1, 0); dfs2(0, s2, siz[s1]);
    }
    cout << ans.m2 << '\n';
    return 0;
}
```