# [Strongly Connected Tournament](https://www.luogu.com.cn/problem/CF913F)

- 首先考虑设 $dp_i$ 表示，$i$ 个点的期望次数
- 考虑枚举一个最菜的联通块
- $dp_x=\sum_{i=1}^x p_{x,i}p_i(dp_i+dp_{x-i}+\frac{i(i-1)}{2}+i(x-i))$
- $dp_x=\frac{\sum_{i=1}^{x-1} p_{x,i}p_i(dp_i+dp_{x-i}+\frac{i(i-1)}{2}+i(x-i))+p_x\frac{x(x-1)}{2}}{1-p_x}$
- 其中 $p_{x,i}$ 表示，$x$ 个点中选出 $i$ 个点的概率
- $p_{x}$ 表示，$x$ 个点为整块的概率
- 显然有 $p_x=1-\sum_{i=1}^{x-1}p_ip_{x,i}$
- 然后 $p_{x,i}$ 又不好算，又得钦定，哎！
- 钦定我们一次从小到大加入每个点
- $p_{x,i}=p^ip_{x-1,i}+(1-p)^{x-i}p_{x-1,i-1}$

```c++
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll N=2020,mod=998244353;
ll ksm(ll a,ll b)
{
	ll ans=1;
	while(b)
    {
		if(b&1)ans=ans*a%mod;
		a=a*a%mod;b>>=1;
	}
	return ans;
} 
ll n,p,c[N],d[N][N],dp[N];
int main()
{
	cin>>n;ll a,b;cin>>a>>b;
	const ll p=a*ksm(b,mod-2)%mod;
	d[1][0]=d[1][1]=1;
    for(int i=2;i<=n;i++)d[i][0]=1;
	for(int i=2;i<=n;i++)for(int j=1;j<=i;j++)
	d[i][j]=(d[i-1][j]*ksm(mod+1-p,j)+d[i-1][j-1]*ksm(p,i-j))%mod;
	for(int i=1;i<=n;i++)
    {
		for(int j=1;j<i;j++)
			c[i]=(c[i]+c[j]*d[i][j])%mod;
		c[i]=1-c[i];
	}
	for(int i=1;i<=n;i++){
		ll res=0;
		for(int j=1;j<i;j++){
			ll tmp=(dp[j]+dp[i-j])%mod;
			tmp=(tmp+j*(i-j))%mod;
			tmp=(tmp+j*(j-1)/2)%mod;
			res=(res+c[j]*d[i][j]%mod*tmp)%mod;
		}
		res=(res+c[i]*d[i][i]%mod*(i*(i-1)/2))%mod;
		dp[i]=res*ksm(mod+1-c[i]*d[i][i]%mod,mod-2)%mod;
	}
	cout<<(dp[n]+mod)%mod<<endl;
}
```