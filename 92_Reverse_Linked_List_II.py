# 92. Reverse Linked List II
from ListNodeModule import ListNode, create_linked_list


def reverseBetween(head: ListNode | None, left: int, right: int) -> ListNode | None:
    _left = None
    prev = None
    curr = head
    i = 1
    if curr is not None:
        while curr is not None and i != left:
            if i == left - 1:
                _left = curr
            curr = curr.next
            i += 1
    _mid = curr
    while curr is not None and i <= right:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
        i += 1
    if _left is not None:
        _left.next = prev
    else:
        head = prev
    if _mid is not None:
        _mid.next = curr
    return head


def main():
    tests = [[[3,5],1,2],[[1, 2, 3, 4, 5], 2, 4], [[5], 1, 1]]
    for test in tests:
        print(f"{test} = {reverseBetween(create_linked_list(test[0]), test[1], test[2])}")


if __name__ == "__main__":
    main()
