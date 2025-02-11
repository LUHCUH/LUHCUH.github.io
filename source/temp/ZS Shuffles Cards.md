# [ZS Shuffles Cards](https://www.luogu.com.cn/problem/CF1392H)

- 若我们取到了鬼牌则会游戏重开，这是离谱的
- 有 $E(ans)=E(重开多少次)E(重开一次摸的牌数)$
- $E(重开一次摸的牌数)=\frac{n}{m+1}+1$
  - 考虑每张数字牌在某一次被摸的概率
  - $P(x)=\frac{1}{m+1}$，因为我们只需考虑所有鬼牌与那一张数字牌的相对位置
  - $E(...)=nP(x)+1$，加的 $1$ 是最后摸鬼牌结束
- $E(重开多少次)$：
  - 我们借助选牌时选到鬼牌后重开来计算期望
  - 设 $f(i)$ 表示我们还有 $i$ 张牌没被取走 $i$ 的期望
  - $f(n)=1$，开局的算一次吧
  - $f(i-1)=\frac{i}{m+i}f(i)+\frac{m}{m+i}(f(i-1)+1)$
  - $f(i-1)=f(i)+\frac{m}{i}$

```c++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll mod=998244353;
ll f[2000200];
ll ksm(ll a,ll b)
{
    ll ans=1;
    while(b){if(b&1)ans=ans*a%mod;b>>=1;a=a*a%mod;}
    return ans;
}
#define inv(x) ksm(x,mod-2)
int main()
{
    ll n,m; cin>>n>>m; f[n]=1;
    for(int i=n;i>=1;i--)
    f[i-1]=(f[i]+m*inv(i))%mod;
    cout<<(n*inv(m+1)+1)%mod*f[0]%mod<<'\n';
    return 0;
}
```