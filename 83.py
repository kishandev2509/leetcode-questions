# 83. Remove Duplicates from Sorted List
from ListNodeModule import ListNode, create_list

def deleteDuplicates(head: ListNode | None) -> ListNode | None:
    if head is not None:
        current = head
        nextt = current.next
        while current.next is not None:
            while nextt is not None and current.val == nextt.val:
                current.next = nextt.next
                nextt = current.next
            current = current.next
            if current is None:
                return head
            else:
                nextt = current.next
    return head
            



def main():
    tests = [[1,1,1],[],[1,1,2],[1,1,2,3,3]]
    for test in tests:
        print(f"{test} = {deleteDuplicates(create_list(test))}")

if __name__ == "__main__":
    main()