#include <stdlib.h>
#include <limits.h>

typedef struct OdpEntry{
    int levelll;
    int val;
} OdpEntry;

void countColsAndLs(struct TreeNode* root, int level, int col, int* min, int* max){
    if(!root) return;
    countColsAndLs(root->left, level+1, col-1, min, max);
    countColsAndLs(root->right, level+1, col+1, min, max);
    if(col < *min){
        *min = col;
    }
    if(col > *max){
        *max = col;
    }
}

OdpEntry* createNew(int value, int levell){
    OdpEntry* res = (OdpEntry*)malloc(sizeof(OdpEntry));
    res->val = value;
    res->levelll = levell;
    return res;
}

void verticalRec(struct TreeNode* root, int level, int col, int offset, int* curr_sizes, int* act_sizes, OdpEntry*** odp){
    if(!root) return;
    else{
        verticalRec(root->left, level+1, col-1, offset, curr_sizes, act_sizes, odp);
        verticalRec(root->right, level+1, col+1, offset, curr_sizes, act_sizes, odp);
        int curr_col = col;
        int value = root->val;
        if(curr_sizes[col+offset] == act_sizes[col+offset]){
            odp[col+offset] = realloc(odp[col+offset], (curr_sizes[col+offset]*2+1)*sizeof(OdpEntry*));
            curr_sizes[col+offset] *= 2;
            curr_sizes[col+offset]++;
        }
        OdpEntry* newOne = createNew(value, level);
        int j = act_sizes[col+offset] - 1;
        while(j >= 0 && odp[col+offset][j]->levelll > level){
            odp[col+offset][j+1] = odp[col+offset][j];
            j--;
        }
        while(j >= 0 && odp[col+offset][j]->val > value && odp[col+offset][j]->levelll == level){
            odp[col+offset][j+1] = odp[col+offset][j];
            j--;
        }
        odp[col+offset][j+1] = newOne;
        act_sizes[col+offset]++;
    }
}

int** verticalTraversal(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if(!root) return NULL;
    int min = INT_MAX;
    int max = INT_MIN;
    countColsAndLs(root, 0, 0, &min, &max);
    *returnSize = max-min+1;
    int** odp = (int**)malloc(sizeof(int*)*(*returnSize));
    for(int i = 0 ; i < *returnSize; i++){
        odp[i] = (int*)malloc(sizeof(int));
    }
    int* curr_sizes = (int*)malloc(sizeof(int)*(*returnSize));
    for(int i = 0 ; i < *returnSize; i++){
        curr_sizes[i] = 0;
    }
    int* act_sizes = (int*)malloc(sizeof(int)*(*returnSize));
    for(int i = 0 ; i < *returnSize; i++){
        act_sizes[i] = 0;
    }
    OdpEntry*** odpEntries = (OdpEntry***)malloc(sizeof(OdpEntry**)*(*returnSize));
    for(int i = 0 ; i < *returnSize; i++){
        odpEntries[i] = (OdpEntry**)malloc(sizeof(OdpEntry*));
    }
    verticalRec(root, 0, 0, -min, curr_sizes, act_sizes, odpEntries);
    *returnColumnSizes = act_sizes;
    for(int i = 0 ; i < *returnSize; i++){
        int j = act_sizes[i];
        odp[i] = (int*)malloc(sizeof(int)*j);
        for(int k = 0 ; k < j ; k++){
            odp[i][k] = odpEntries[i][k]->val;
        }
    }
    return odp;
}
