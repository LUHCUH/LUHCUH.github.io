---
title: 对称旅行者
message: dsfz NOI篇 的密码
tags:
  - accnoi
  - 期望
date: 2024-11-14 18:34:37
---
### [ 对称旅行者](http://47.92.197.167:5283/contest/570/problem/4)
- 题目简述
- 数轴上有 $n$ 个点 $x_1,x_2,\dots,x_n$，每轮进行 $m$ 次操作，每次给定一个点 $p$，令 $x_p$ 位移到关于 $x_{p-1}$ 或 $x_{p+1}$ 的对称点上，共进行 $k$ 轮，求对于每个 $i$，$x_i$ 每种情况下的位置和。

- $n,m\le 10^5$，$k\le 10^{18}$。

- 题解：
- 我们可以用期望的角度转化问题，设 $f_i$ 为 $x_i$ 的期望，则在进行一次操作之后，$f_p\gets f_{p-1}+f_{p+1}-f_p$。

- 观察上述式子，我们不难发现从几何意义上，相当于 $f_p$ 位移到关于 $f_{p-1}$ 与 $f_{p+1}$ 中点的对称点上。我们不妨设 $g_i=f_{i+1}-f_i$，上式也就可以转化为了交换 $g_{p-1}$ 与 $g_p$。

- 现在我们可以用 $O(m)$ 的时间求出一轮的最终情况，观察到 $k$ 非常大，这启示我们记录转移的方式，用类似矩阵乘法快速幂的形式解决问题。

- 复杂度 $O(m+n\log k)$。

### code
```c++
#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N=1e5+10;
const int P=1e9+7;
int n,m,k,a[N],c[N];
inline int qpow(int x,int y){
    int ans=1;
    while(y){
        if(y&1) ans=ans*x%P;
        x=x*x%P; y>>=1;
    }
    return ans;
}
struct Node{int to[N];}base,cur;
Node operator*(Node x,Node y){
    Node z;
    for(int i=1;i<n;i++)
        z.to[i]=y.to[x.to[i]];
    return z;
}
Node qpow(Node x,int y){
    Node ans;
    for(int i=1;i<n;i++)ans.to[i]=i;
    while(y){
        if(y&1)ans=ans*x;
        x=x*x; y>>=1;
    }
    return ans;
}
signed main(){
    freopen("travel.in","r",stdin);
    freopen("travel.out","w",stdout);
    scanf("%lld",&n);
    for(int i=1;i<=n;i++)scanf("%lld",a+i);
    for(int i=1;i<n;i++)c[i]=a[i+1]-a[i];
    for(int i=1;i<n;i++)cur.to[i]=base.to[i]=i;
    scanf("%lld%lld",&m,&k);
    for(int i=1;i<=m;i++){
        int x;scanf("%lld",&x);
        swap(base.to[x-1],base.to[x]);
    }
    cur=cur*qpow(base,k);
    int ans=0;
    for(int i=1;i<=n;i++){
        if(i>1)a[i]=a[i-1]+c[cur.to[i-1]];
        printf("%lld ",(a[i]%P+P)%P*qpow(qpow(2,m),k)%P);
    }
    puts("");
    return 0;
}
```