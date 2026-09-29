int knightDialer(int n) {
    long answer = 0;
    int mod = 1000000007;
    long dp[n+1][10];
    dp[1][0] = dp[1][1] = dp[1][2] = dp[1][3] = dp[1][4] = dp[1][5] = dp[1][6] = dp[1][7] = dp[1][8] = dp[1][9] = 1;
    for(int i = 2; i <= n; i++){
        dp[i][0] = (dp[i-1][7]%mod+dp[i-1][5]%mod)%mod;
        dp[i][1] = (dp[i-1][6]%mod+dp[i-1][8]%mod)%mod;
        dp[i][2] = (dp[i-1][3]%mod+dp[i-1][7]%mod)%mod;
        dp[i][3] = (dp[i-1][8]%mod+dp[i-1][2]%mod+dp[i-1][9]%mod)%mod;
        dp[i][4] = 0;
        dp[i][5] = (dp[i-1][0]%mod+dp[i-1][6]%mod+dp[i-1][9]%mod)%mod;
        dp[i][6] = (dp[i-1][1]%mod+dp[i-1][5]%mod)%mod;
        dp[i][7] = (dp[i-1][0]%mod+dp[i-1][2]%mod)%mod;
        dp[i][8] = (dp[i-1][3]%mod+dp[i-1][1]%mod)%mod;
        dp[i][9] = (dp[i-1][3]%mod+dp[i-1][5]%mod)%mod;
    }
    for(int i = 0; i <= 9; i++){
        answer += dp[n][i]%mod;
        answer %= mod;
    }
    return answer;
}
