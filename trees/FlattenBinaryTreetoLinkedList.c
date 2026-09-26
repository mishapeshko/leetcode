void flatRec(struct TreeNode* root, struct TreeNode** prev){
    if(!root) return;
    struct TreeNode* l = root->left;
    struct TreeNode* r = root->right;
    if(*prev){
        (*prev)->right = root;
    }
    *prev = root;
    root->left = NULL;
    flatRec(l, prev);
    flatRec(r, prev);
}

void flatten(struct TreeNode* root) {
    struct TreeNode* prev = NULL;
    flatRec(root, &prev);    
}
