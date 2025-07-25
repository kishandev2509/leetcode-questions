# 86. Partition List

from ListNodeModule import ListNode, create_linked_list

def partition(head: ListNode | None, x: int) -> ListNode | None:
    if head is not None:
        temp = head
        before = result_before = ListNode()
        after = result_after = ListNode()
        while temp is not None:
            if temp.val < x:
                before.next = temp
                before = before.next
            else:
                after.next = temp
                after = after.next
            temp = temp.next
        before.next = None
        after.next = None
        before.next = result_after.next
        return result_before.next
    

def main():
    tests = [[[1,4,3,2,5,2],3],[[2,1],2]]
    for test in tests:
        print(f"{test} = {partition(create_linked_list(test[0]),test[1])}")

if __name__ == "__main__":
    main()