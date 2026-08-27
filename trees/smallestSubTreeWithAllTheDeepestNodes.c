void checkDepth(struct TreeNode* root, int level, int* max_depth, int* howM_max){
    if(!root) return;
    if(level == *max_depth){
        (*howM_max)++;
    }
    if(level > *max_depth){
        *max_depth = level;
        *howM_max = 1;
    }
    checkDepth(root->left, level+1, max_depth, howM_max);
    checkDepth(root->right, level+1, max_depth, howM_max);
}

void checkDeepest(struct TreeNode* root, struct TreeNode** odp, int howM_max, int* howM, int level, int max_depth){
    if(*odp){
        return;
    }
    if(!root){
        *howM = 0;
        return;
    }
    int howM_l = 0, howM_r = 0;
    checkDeepest(root->left, odp, howM_max, &howM_l, level+1, max_depth);
    checkDeepest(root->right, odp, howM_max, &howM_r, level+1, max_depth);
    if(*odp) return;
    if(howM_l+howM_r == howM_max){
        *odp = root;
        return;
    }
    if(level == max_depth){
        *howM = howM_l+howM_r+1;
        if(*howM == howM_max){
            *odp = root;
        }
        return;
    }
    *howM = howM_l+howM_r;
    return;
}

struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {
    if(!root) return root;
    int max_depth = -1;
    int howM_max = 0;
    checkDepth(root, 0, &max_depth, &howM_max);
    int howM = 0;
    struct TreeNode* odp = NULL;
    checkDeepest(root, &odp, howM_max, &howM, 0, max_depth);
    return odp;
}
