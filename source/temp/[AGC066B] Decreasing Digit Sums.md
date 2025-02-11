# [[AGC066B] Decreasing Digit Sums](https://www.luogu.com.cn/problem/AT_agc066_b)

- 我们要使 $f(2^n)>f(2\times 2^n)$
- 这里并没有什么好的想法，那就试一试
- 发现 $2\times 5$ 会发生进位，有利于形成 $f(2^n)>f(2\times 2^n)$ 的局面
- 构造 $x=\overline{5^n...5^35^25}$，你 $n$ 大一点就好啦，呱！
- 又是一个我够造不出来的题，哎！