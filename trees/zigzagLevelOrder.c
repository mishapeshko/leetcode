void countLevels(struct TreeNode* root, int* levels, int level){
    if(!root) return;
    if(level > *levels){
        *levels = level;
    }
    countLevels(root->left, levels, level+1);
    countLevels(root->right, levels, level+1);
}

void findMax(struct TreeNode* root, int level, int* maks, int* tab){
    if(!root) return;
    tab[level]++;
    if(tab[level] > *maks){
        *maks = tab[level];
    }
    findMax(root->left, level+1, maks, tab);
    findMax(root->right, level+1, maks, tab);
}

void leftPreOrder(struct TreeNode* root, int** odp, int* tab, int level){
    if(!root) return;
    if(level%2 == 0){
        odp[level][tab[level]++] = root->val;
    }
    leftPreOrder(root->left, odp, tab, level+1);
    leftPreOrder(root->right, odp, tab, level+1);
}

void rightPreOrder(struct TreeNode* root, int** odp, int* tab, int level){
    if(!root) return;
    if(level%2 == 1){
        odp[level][tab[level]++] = root->val;
    }
    rightPreOrder(root->right, odp, tab, level+1);
    rightPreOrder(root->left, odp, tab, level+1);
}

int** zigzagLevelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if(!root){
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int levels = 1;
    countLevels(root, &levels, 1);
    *returnSize = levels;
    int** odp = (int**)malloc(sizeof(int*)*(*returnSize));
    int maks = 0;
    int* tab = (int*)malloc(sizeof(int)*levels);
    for(int i = 0; i < levels; i++){
        tab[i] = 0;
    }
    findMax(root, 0, &maks, tab);
    for(int i = 0; i < levels; i++){
        odp[i] = (int*)malloc(sizeof(int)*maks);
        tab[i] = 0;
    }
    leftPreOrder(root, odp, tab, 0);
    rightPreOrder(root, odp, tab, 0);
    *returnColumnSizes = tab;
    return odp;
}
