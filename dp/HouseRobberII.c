#define MIN_V -1001

int max(int a, int b){
    return a > b ? a : b;
}

int rob(int* nums, int numsSize) {
    if(numsSize == 1){
        return nums[0];
    }
    int dp[2][numsSize];
    for(int i = 0; i <= 1; i++){
        for(int j = 0; j < numsSize; j++){
            dp[i][j] = 0;
        }
    }
    dp[1][0] = MIN_V;
    for(int i = 1; i < numsSize; i++){
        dp[0][i] = max(dp[0][i-1], dp[1][i-1]);
        dp[1][i] = nums[i]+dp[0][i-1];
    }
    int res1 = max(dp[0][numsSize-1], dp[1][numsSize-1]);
    dp[0][0] = 0;
    dp[1][0] = nums[0];
    for(int i = 1; i < numsSize; i++){
        dp[0][i] = max(dp[0][i-1], dp[1][i-1]);
        dp[1][i] = nums[i]+dp[0][i-1];
    }
    int res2 = dp[0][numsSize-1];
    return max(res1, res2);
}
