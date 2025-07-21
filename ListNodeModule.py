# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        result = ""
        nodes = set()
        curr = self
        while curr is not None and curr not in nodes:
            result+=f"{curr.val}->"
            nodes.add(curr)
            curr = curr.next
        result += "None" if curr is None else "Loop"
        return result


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
