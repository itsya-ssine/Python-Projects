struct ListNode
{
    int val;
    struct ListNode* next;
};

// Odd Even Linked List

// Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

// The first node is considered odd, and the second node is even, and so on.

// Note that the relative order inside both the even and odd groups should remain as it was in the input.

// You must solve the problem in O(1) extra space complexity and O(n) time complexity.



struct ListNode* oddEvenList(struct ListNode* head) {
    if (!head || !head->next) {
        return head;
    }

    struct ListNode* odd = head;
    struct ListNode* even = head->next;
    struct ListNode* evenHead = even;  // Save the head of the even list

    while (even && even->next) {
        odd->next = even->next;  // Link odd nodes
        odd = odd->next;         // Move odd pointer
        even->next = odd->next;  // Link even nodes
        even = even->next;       // Move even pointer
    }

    odd->next = evenHead;  // Combine the odd and even lists

    return head;
}