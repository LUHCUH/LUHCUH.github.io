---
title: 数位
message: dsfz NOI篇 的密码
tags:
  - accnoi
  - 数论
date: 2024-11-14 18:29:52
---
### [数位](http://47.92.197.167:5283/contest/554/problem/1)

- 题目简述：
- 给一个整数 $d$，和一个字符串 $s$。若一个字符串转十进制去前导零后为 $d$ 的倍数，称之为好串。
- 现在要给字符串 $s$ 划分成若干段，使得相邻两段子串中有一个子串是好串。求划分方案数
- 题解：
- 首先很容易想到 $dp_{i,0/1}$ 表示上一段，段末是 $i$，且是（不好/好）段的方案数。
- 转移是简单了，重点在于判断一个字符串是否是 $d$ 的倍数
- **这里考虑 $s\equiv 0\pmod d $。不妨设 $h_i=h_{i-1}\times 10+s_i$，$p_i=p_{i-1}\times 10$**
- **我们有 $[l+1,r]$ 是好段，当且仅当 $h_{r}-h_{l}*p_{r-l}\equiv 0\pmod d$**。
- 接着我们考虑优化 $O(n^2)$ 的 $dp$。注意到，转移只有两部分，即与 $h_r$ 同余，与 $h_r$ 不同余。
- 由注意到 $h_l$ 随着 $r$ 的增大，对 $h_r$ 的相对贡献会不断 $\times 10$，我们不放设一个全局权，记作 $q$，使得 $h'_l\times q$ 等于真实的 $h_l*p_{r-l}$，而 $h_l*p_{r-l}\div q$ 作为 $h'_l$。这里只可意会，和单调队列有异曲同工之妙。
- 反思：这样做真的对吗？其实是不对的，因为随着 $r$ 的增大 $q$ 不断乘 $10$。这时若有 $p$ 在模意义下等于 $0$ 我们边不能做 $\div q$ 的操作。
- 解决办法很简单，考虑对 $d$ 分解为 $2^x 5^y d'$，我们只需要保证，模三者同时为 $0$ 即可。
- 这样的话，记录向上文那么做就不太方便，具体是因为只有一个桶我们只能记录 $d'$ 是否合法的情况，其他情况考虑不了。
- 注意到 $20\le r-l$ 的时候，$p_{r-l}$ 在 $2,5$ 的情况都余 $0$。这要求 $h_{l}$ 也得是 $0$，否则一定不合法。而我们只需要对于大于 $20$ 的那些位置开桶记录权值和即可，自然地 $q$ 等，就是在模 $d'$ 的意义下的了
- 对于小于 $20$ 的我们暴力算。
- 这里题解有一种神奇的写法，其实和单调队列还是一样。
- **$h_l\times p_{r-l}=h_r$ 等价于 $h_l\times p_{n-l}=h_r\times p_{n-r}$。这有什么好处呢，桶的位置不用滚动 $q$ 了，可以直接算。**

- 补充：$0$ 是任何非 $0$ 自然数的倍数（我才知道）

``` c++
#include <bits/stdc++.h>
using namespace std; const int N = 100100;
typedef long long ll; const ll mod = 1000000007;
ll dp[N][2], t[N * 10][2], h[N], hd[N], p[N], d, d1, d2;
int cnt(ll x, int num) { int s = 0; while (x % num == 0)x /= num, s++; return s; }
void work()
{
	string s; cin >> s >> d; p[0] = 1;
	int c2 = 0, c5 = 0; d1 = d; d2 = 1;
	while (d1 % 2 == 0)d1 /= 2, d2 *= 2, c2++;
	while (d1 % 5 == 0)d1 /= 5, d2 *= 5, c5++;
	const int n = s.size(), m = max(c2, c5) + 1;

	for (int i = 1; i <= n; i++)p[i] = p[i - 1] * 10 % d;
	for (int i = 1; i <= n; i++)h[i] = (h[i - 1] * 10 + s[i - 1] - '0') % d, hd[i] = h[i] % d1;
	for (int i = 0; i < d; i++)t[i][0] = t[i][1] = 0;

	dp[0][1] = 1; ll sum = 0;
	for (int i = 1; i <= n; i++)
	{
		dp[i][1] = 0; dp[i][0] = 0; hd[i] = h[i] * p[n - i] % d1;
		for (int j = max(0, i - m); j < i; j++)
		{
			if ((h[i] - p[i - j] * h[j]) % d == 0)dp[i][1] += dp[j][0] + dp[j][1];
			else dp[i][0] += dp[j][1];
		}
		if (i - m - 1 >= 0)
		{
			ll x = 0;
			if (h[i] % d2 == 0)
			{
				x = t[hd[i]][1];
				dp[i][1] += x + t[hd[i]][0];
			}
			dp[i][0] += sum - x;
		}
		dp[i][0] %= mod; dp[i][1] %= mod;
		if (i - m >= 0)
		{
			t[hd[i - m]][0] += dp[i - m][0];
			t[hd[i - m]][1] += dp[i - m][1];
			sum += dp[i - m][1];
		}
	}
	cout << ((dp[n][0] + dp[n][1]) % mod + mod) % mod << '\n';
}
int main()
{
	freopen("digit.in", "r", stdin);
	freopen("digit.out", "w", stdout);
	ios::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	int T; cin >> T; while (T--) work(); return 0;
}
```