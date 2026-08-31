int min(int a, int b){
    return a < b ? a : b;
}

int trap(int* height, int heightSize) {
    int* fromLeft = (int*)malloc(sizeof(int)*(heightSize));
    int* fromRight = (int*)malloc(sizeof(int)*(heightSize));
    fromLeft[0] = -1;
    fromRight[heightSize-1] = -1;
    int maxR = 0;
    for(int i = 1; i < heightSize; i++){
        if(height[maxR] > height[i]){
            fromLeft[i] = maxR;
        }
        else{
            fromLeft[i] = -1;
        }
        if(height[maxR] < height[i]){
            maxR = i;
        }
    }
    int maxL = heightSize-1;
    for(int j = heightSize-2; j>=0; j--){
        if(height[maxL] > height[j]){
            fromRight[j] = maxL;
        }
        else{
            fromRight[j] = -1;
        }
        if(height[maxL] < height[j]){
            maxL = j;
        }
    }
    long long res = 0;
    for(int k = 0; k < heightSize; k++){
        if(fromLeft[k]!=-1&&fromRight[k]!=-1){
            res += min(height[fromLeft[k]], height[fromRight[k]])-height[k];
        }
    }
    return res;
}
