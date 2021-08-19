#https://twitter.com/e869120/status/1397684795560259586/photo/1
#動的計画法(DP)
#類題 ABC129C
n,l = map(int,input().split())
mod = 10**9+7
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
  if i < l:
    dp[i] = dp[i-1]
  else:
    dp[i] = dp[i-1] + dp[i-l]
  dp[i] %= mod
print(dp[-1])