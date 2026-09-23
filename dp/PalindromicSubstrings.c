int len(char* s){
    int i = 0;
    while(s[i] != '\0'){
        i++;
    }
    return i;
}

int max(int a, int b){
    return a > b ? a : b;
}

int countSubstrings(char* s) {
    int n = len(s);
    int dp[n][n];
    int counter = n;
    for(int i = 0; i < n; i++){
        dp[i][i] = 1;
    }
    for(int i = n-1; i >= 0; i--){
        for(int j = i+1; j < n; j++){
            if(s[i] == s[j]){
                if(i+1<=j-1){
                    dp[i][j] = dp[i+1][j-1]+2;
                }
                else{
                    dp[i][j] = 2;
                }
                if(dp[i][j] == j-i+1){
                    counter++;
                }
            }
            else{
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
            }
        }
    }
    return counter;
}
