int findMin(int* nums, int numsSize) {
    int val = nums[0];
    int left = 0;
    int right = numsSize-1;
    while(left < right){
        int mid = left+(right-left)/2;
        if(nums[mid] >= val){
            left = mid+1;
        }
        else{
            right = mid;
        }
    }
    return nums[left] > val ? val : nums[left];
}
