int checkRecord(int n) {
    int mod = 1000000007;
    long dp[n+1][3][2];
    for(int i = 0; i<=n; i++){
        for(int j = 0; j <= 2; j++){
            for(int k = 0; k <= 1; k++){
                dp[i][j][k] = 0;
            }
        }
    }
    long answer = 0;
    dp[0][0][0] = 1;
    for(int i = 1; i <= n; i++){
        long sum = 0;
        for(int j = 0; j<=2; j++){
            sum += dp[i-1][j][0]%mod;
        }
        dp[i][0][0] = sum%mod;
        long newSum = 0;
        for(int j = 0; j<=2; j++){
            newSum += dp[i-1][j][1]%mod;
        }
        dp[i][0][1] = (sum%mod+newSum%mod)%mod;
        for(int j = 1; j<=2; j++){
            dp[i][j][0] = dp[i-1][j-1][0]%mod;
        }
        for(int j = 1; j<=2; j++){
            dp[i][j][1] = dp[i-1][j-1][1]%mod;
        }
    }
    for(int j = 0; j <= 2; j++){
        for(int k = 0; k<=1; k++){
            answer += dp[n][j][k]%mod;
        }
    }
    return answer%mod;
}
