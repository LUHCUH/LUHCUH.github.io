---
title: 软件工程
tags:
  - accnoi
date: 2024-11-14 18:37:40
---
### [软件工程](http://47.92.197.167:5283/contest/558/problem/3)

- 题目简述：给你 $n$ 个区间，$k$ 个集合，把区间放到 $k$ 集合中不可以不放。一个集合的代价为区间的交（公共部分）。求 $k$ 个集合代价的最大值
- 题解：
- 首先，可定有一种感觉的理解，一个集合里放的所有数一定是相邻的，相邻的不好描述，但感知上就是。
- 而区间的关系是错综复杂的，**但有一点，如果只保留所有不包含任何其他区间的区间的话。有区间所有端点，排序后同时单调递增**。
- **同样的，如果只保留不被任何区间包含的区间的话。左右端点也是单调递增的**。
- 接着，发现若所有区间左端点递增，右端点也递增。每一个集合必然是由一段连续的区间组成的。这里没有复杂的关系，很好理解。
- 这启发我们考虑，分离区间的包含关系。
- 注意到若一区间 $x$ 包含了区间 $y$。那么集合里选了 $y$，再选 $x$ 不会有任何负的贡献。而若是 $x$ 不与 $y$ 在同一集合，那就需要 $x$ 所在的集合只有 $x$ 自己。因为，若是存在其他区间 $z$。$x$ 的加入不会造成任何正贡献，那莫不如，$x$ 加入 $y$ 所在的集合呢。
- 分析到了上述部分，剩下的就简单多了。我们把所有小的区间，就是不包含任何其他区间的区间，拿出来 $dp$。其他的区间用优先队列，不断地选最大值。
- 设 $dp_{i,j}$ 表示选了 $i$ 个集合，选到了 $j$ 的最大贡献。转移是简单的。统计答案时只需要合并 选了 $i$ 个 $dp$ 集合，$k-i$ 个非 $dp$ 集合，就是优先队列的前 $k-i$ 大的区间独立构成集合。再之后的就是简单的。
- 但是，感觉终究是感觉，总有那么一种情况能极端的，跨膜运输区间，就是有集合交为 $0$，这时候就不罐子破摔，干脆除了前 $k-1$ 大的都放进去。剩下的 $k-1$ 大的最为答案。于是本题结束

```c++
#include <bits/stdc++.h>
using namespace std;
const int N = 5100;
#define int long long
struct node { int l, r; }a[N], b[N];
priority_queue<int> q, p;
int dp[N][N], R[1000100], mx[N], top;
signed main()
{
    freopen("se.in", "r", stdin);
    freopen("se.out", "w", stdout);
    memset(R, 0x3f, sizeof R);
    int n, m, ans = 0; cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i].l >> a[i].r;
        if (R[a[i].l] <= a[i].r)p.push(a[i].r - a[i].l);
        else if (R[a[i].l] != 0x3f3f3f3f3f3f3f3f)p.push(R[a[i].l] - a[i].l);
        R[a[i].l] = min(R[a[i].l], a[i].r);
    }
    for (int i = 1; i <= n; i++) q.push(a[i].r - a[i].l);
    for (int i = 1; i <= m - 1; i++)ans += q.top(), q.pop();
    int ma = 0x3f3f3f3f3f3f3f3f - 1;
    for (int i = 1000000; i >= 1; i--)if (R[i] != 0x3f3f3f3f3f3f3f3f)
    {
        if (R[i] >= ma)p.push(R[i] - i);
        else ma = R[i], b[++top] = { i,R[i] };
    }
    for (int i = 1; p.size(); i++) mx[i] = p.top() + mx[i - 1], p.pop();
    memset(dp, 0xc2, sizeof dp);
    dp[0][0] = 0;
    for (int i = 1; i <= m && i <= top; i++)
        for (int j = i; j <= top; j++)
            for (int k = 0; k < j; k++)
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + b[j].r - b[k + 1].l);
    for (int i = 0; i <= m && i <= top; i++)ans = max(ans, dp[i][top] + mx[m - i]);
    cout << ans << '\n';
    return 0;
}

```