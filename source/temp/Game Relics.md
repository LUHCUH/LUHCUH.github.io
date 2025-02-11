# [Game Relics](https://www.luogu.com.cn/problem/CF1267G)

- 首先猜一下(在 $x\le c_i$ 的条件下)，应该先抽奖，后剩下的全买
- 考虑已经拥有了 $k$ 个圣物，再又有一个圣物的期望代价为
  - $E(X)=\frac{n-k}{n}x+\frac{k}{n}(E(X)+\frac{x}{2})$
  - $E(X)=x(1+\frac{k}{2(n-k)})$
- 随着随机选择，设还剩 $k$ 个圣物没有，其代价和为 $s$
  - 若直接买下 $E(Buy)=\frac{s}{k}$
  - 若继续抽奖 $E(Rand)=x(1+\frac{k}{2(n-k)})$
  - 对于每种情况 $E(Real)=min(E(Buy),E(Rand))$ 代价是最优的
- 于是设 $f_{i,c}$ 表示还剩 $i$ 个数没选，没选数的代价和为 $c$ 的方案数
- $f_{k+1,c}=\sum f_{k,c-c_i}$
- 我们只需要决策好每一个状态下一个选那个期望最优，然后成上概率就好了
- 具体的 $\frac{f_{k,c}}{\binom{n}{k}}E(Real)$ 就行了

```c++
#include <bits/stdc++.h>
using namespace std;
typedef double db;
const int N=110,C=10100;
int n,sum,v[N]; db x,dp[N][C];
int main()
{
    scanf("%d%lf",&n,&x); db ans=0; dp[0][0]=1;
    for(int i=1;i<=n;i++) scanf("%d",&v[i]), sum+=v[i];
    for(int i=1;i<=n;i++) for(int k=i-1;k>=0;k--)
    for(int c=v[i];c<=sum;c++)
    dp[k+1][c]+=dp[k][c-v[i]]*(k+1)/(n-k);
    for(int k=1;k<=n;k++)for(int s=0;s<=sum;s++)
    ans+=min(1.0*s/k,x*(1+1.0*(n-k)/(2*k)))*dp[k][s];
    printf("%.9lf\n",ans);
    return 0;
}
```