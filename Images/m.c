
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* middle = head;
    struct ListNode* end = head;

    while (end && end->next) {
        middle = middle->next;
        end = end->next->next;
    }
    return middle;
}

struct ListNode* middleNode(struct ListNode* head) {     
    // Slow pointer to find the middle node
    struct ListNode* middle = head;     
    // Fast pointer to reach the end of the list
    struct ListNode* end = head;      

    // Traverse the list:
    while (end && end->next) {  
        middle = middle->next; // Move slow pointer one step
        end = end->next->next; // Move fast pointer two steps
    }

    // When fast pointer reaches the end
    // Slow pointer will be at the middle
    return middle; 
}