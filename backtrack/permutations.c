void merge(int* arr, int len, int left, int right){
    if(left >= right) return;
    int mid = left+(right-left)/2;
    int* elem = (int*)malloc((right-left+1)*sizeof(int));
    int i = left;
    int j = mid+1;
    int k = 0;
    while(i <= mid || j <= right){
        if(i > mid){
            elem[k++] = arr[j++];
        }
        else if(j > right){
            elem[k++] = arr[i++];
        }
        else if(arr[i] < arr[j]){
            elem[k++] = arr[i++];
        }
        else{
            elem[k++] = arr[j++];
        }
    }
    for(int p = left; p<=right; p++){
        arr[p] = elem[p-left];
    }
    free(elem);
}

void merges(int* arr, int len, int left, int right){
    if(left == right) return;
    int mid = left + (right-left)/2;
    merges(arr, len, left, mid);
    merges(arr, len, mid+1, right);
    merge(arr, len, left, right);
}

void mergesort(int* arr, int len){
    int left = 0;
    int right = len-1;
    merges(arr, len, left, right);
}

int* copy(int* arr, int len){
    int* res = (int*)malloc(sizeof(int)*len);
    for(int j = 0; j < len; j++){
        res[j] = arr[j];
    }
    return res;
}

void nextPerm(int* arr, int len){
    int j = len-1;
    int pop = -11;
    while(j>=0 && pop < arr[j]){
        pop = arr[j];
        j--;
    }
    if(j<0) return;
    int l = j+1;
    int minV = arr[l];
    int min_o = j+1;
    for(int o = l; o < len; o++){
        if(arr[o] > arr[j] && arr[o] < minV){
            minV = arr[o];
            min_o = o;
        }
    }
    arr[min_o] = arr[j];
    arr[j] = minV;
    int u = len-1;
    while(l < u){
        int temp = arr[l];
        arr[l] = arr[u];
        arr[u] = temp;
        l++;
        u--;
    }
    return;
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int ret = 1;
    for(int i = 2; i <= numsSize; i++){
        ret *= i;
    }
    *returnSize = ret;
    int** res = (int**)malloc(sizeof(int*)*(*returnSize));
    int* columnSizes = (int*)malloc(sizeof(int)*ret);
    for(int i = 0; i < ret; i++){
        columnSizes[i] = numsSize;
    }
    *returnColumnSizes = columnSizes;
    mergesort(nums, numsSize);
    int counter = 0;
    while(counter < ret){
        int* dod = copy(nums, numsSize);
        res[counter++] = dod;
        nextPerm(nums, numsSize);
    }
    return res;
}
