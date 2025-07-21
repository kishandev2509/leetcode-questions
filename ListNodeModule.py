# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {repr(self.next)}"


def create_list(listt: list) -> ListNode | None:
    head = None
    temp = head
    for num in listt:
        if temp is None:
            head = temp = ListNode(val=num)
        else:
            temp.next = ListNode(val=num)
            temp = temp.next
    return head
