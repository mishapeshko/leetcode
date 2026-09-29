int countVowelPermutation(int n) {
    long dp[n+1][5];
    int mod = 1000000007;
    dp[1][0] = dp[1][1] = dp[1][2] = dp[1][3] = dp[1][4] = 1;
    for(int i = 2; i<=n; i++){
        dp[i][0] = (dp[i-1][1]%mod+dp[i-1][4]%mod + dp[i-1][2]%mod)%mod;
        dp[i][1] = (dp[i-1][0]%mod+dp[i-1][2]%mod)%mod;
        dp[i][2] = (dp[i-1][1]%mod+dp[i-1][3]%mod)%mod;
        dp[i][3] = dp[i-1][2]%mod;
        dp[i][4] = (dp[i-1][3]%mod+dp[i-1][2]%mod)%mod;
    }
    long answer = 0;
    for(int i = 0; i <= 4; i++){
        answer += dp[n][i]%mod;
        answer %= mod;
    }
    return answer;
}
