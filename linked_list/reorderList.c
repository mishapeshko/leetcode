int len(struct ListNode* head){
    int res = 0;
    while(head){
        res++;
        head = head->next;
    }
    return res;
}

void reorderList(struct ListNode* head) {
    int n = len(head);
    int i = 0;
    struct ListNode* curr = head;
    struct ListNode* h1 = head;
    while(i < (n-1)/2){
        curr = curr->next;
        i++;
    }
    struct ListNode* h2 = curr->next;
    curr->next = NULL;
    struct ListNode* prev = NULL;
    curr = h2;
    while(curr){
        struct ListNode* nast = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nast;
    }
    h2 = prev;
    struct ListNode* l_res = h1;
    struct ListNode* res_head = l_res;
    h1 = h1->next;
    while(h1 && h2){
        struct ListNode* h2_next = h2->next;
        struct ListNode* h1_next = h1->next;
        l_res->next = h2;
        l_res = h2;
        l_res->next = h1;
        l_res = h1;
        h2 = h2_next;
        h1 = h1_next;
        l_res->next = NULL;
    }
    if(h1){
        l_res->next = h1;
        l_res = h1;
    }
    if(h2){
        l_res->next = h2;
        l_res = h2;
    }
    l_res->next = NULL;
    head = res_head;
}
