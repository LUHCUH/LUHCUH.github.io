# [[AGC066A] Adjacent Difference](https://www.luogu.com.cn/problem/AT_agc066_a)

- 考虑我们生成的矩阵中的数都是 $d$ 的倍数
- 我们显然只需要保证 $a'_{i,j}=xd$ 中的 $x$ 互不相同即可
- 我们钦定根据 $i+j$ 的奇偶性来设置 $x$ 为 $0$ 或 $1$，$a_{i,j}\equiv xd\pmod{2d}$
- 我们尝试只对 $x=0$ 时分析它此时的代价，$x=1$ 只需在模意义下相对平移 $d$ 即可
  - 若 $a_{i,j}\bmod 2d\le d$，$a_{i,j}$
  - 若 $d<a_{i,j}\bmod 2d$，$2d-a_{i,j}$
- 此时的最坏代价可以达到 $n^2d$
- 但我们发现有机可乘：考虑构造
  - 若 $a_{i,j}\bmod 2d\le d$，$d-a_{i,j}$
  - 若 $d<a_{i,j}\bmod 2d$，$a_{i,j}-d$
- 若这种存在这样的贡献则与之前的贡献和为 $n^2d$，那么两个中至少有一个符合答案
- 而这恰好是对 $x=1$ 分析的情况
- 这就说明第一种 $x=(i+j)\pmod 2$
- 第二种 $x=(i+j+1)\pmod 2$

```c++
#include <bits/stdc++.h>
using namespace std;
const int N=510;
int a[N][N],b[N][N];
int main()
{
    int n,d,dd,cost=0; cin>>n>>d; dd=d<<1;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
    cin>>a[i][j],b[i][j]=a[i][j];
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
    {
        int x=(a[i][j]%dd+dd)%dd;
        if((i+j)&1)
        {
            int t=x-d;a[i][j]-=t;cost+=abs(t);
            b[i][j]-=(x<=d)?x:x-2*d;
        }
        else
        {
            int t=x-d;b[i][j]-=t;
            a[i][j]-=(x<=d)?x:x-2*d;
            cost+=min(abs(x),abs(x-2*d));
        }
    }
    if(2*cost<=n*n*d)
    {
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            cout<<a[i][j]<<" ";
            cout<<endl;
        }
    }
    else
    {
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            cout<<b[i][j]<<" ";
            cout<<endl;
        }
    }
    return 0;
}
```