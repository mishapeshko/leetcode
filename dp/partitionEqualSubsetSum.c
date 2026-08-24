int sumOf(int* nums, int numsSize){
    int res = 0;
    for(int i = 0; i < numsSize; i++){
        res += nums[i];
    }
    return res;
}

bool canPartition(int* nums, int numsSize) {
    int sum = sumOf(nums, numsSize);
    if(sum % 2 == 1) return false;
    int target = sum / 2;
    bool dp[numsSize+1][target+1];
    for(int i = 0; i <= target; i++){
        dp[0][i] = false;
    }
    for(int i = 0; i <= numsSize; i++){
        if(i != numsSize && nums[i] > target) return false;
        dp[i][0] = true;
    }
    for(int i = 1; i <= numsSize; i++){
        int val = nums[i-1];
        for(int j = 1; j<=target; j++){
            if(dp[i-1][j]) dp[i][j] = true;
            else{
                if(j-val >= 0 && dp[i-1][j-val]){
                    dp[i][j] = true;
                }
                else{
                    dp[i][j] = false;
                }
            }
        }
    }
    return dp[numsSize][target];
}
