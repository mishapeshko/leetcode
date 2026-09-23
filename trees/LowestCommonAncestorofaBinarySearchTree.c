void lcaRec(struct TreeNode* root, struct TreeNode** res, int p, int q){
    if(!root || *res) return;
    if(root->val > p && root->val > q){
        lcaRec(root->left, res, p, q);
    }
    else if(root->val < p && root->val < q){
        lcaRec(root->right, res, p, q);
    }
    else{
        *res = root;
        return;
    }
}

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    struct TreeNode* res = NULL;
    lcaRec(root, &res, p->val, q->val);
    return res;
}
