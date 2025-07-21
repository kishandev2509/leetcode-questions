# 19. Remove Nth Node From End of List
from ListNodeModule import ListNode, create_list


def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    cur = head
    for _ in range(n + 1):
        if cur is None and _ == n :
            return head.next # type: ignore
        if cur is not None:
            cur = cur.next
        else:
            return None
    prev = head
    while cur is not None and prev is not None:
        cur = cur.next
        prev = prev.next
    if prev is not None and prev.next is not None:
        prev.next = prev.next.next
    if prev is None:
        return None
    return head


def main():
    tests = [[[1,2],2],[[1], 1], [[1, 2, 3, 4, 5], 2], [[1, 2], 1]]
    for test in tests:
        print(f"{test} = {removeNthFromEnd(create_list(test[0]), test[1])}")


if __name__ == "__main__":
    main()
