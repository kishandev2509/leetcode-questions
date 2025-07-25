from ListNodeModule import ListNode, create_linked_list
        
def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list2 is None:
        return list1
    if list1 is None:
        return list2
        
    if list1.val <= list2.val:
        temp = result = list1
        list1 = list1.next
    else:
        temp = result = list2
        list2 = list2.next
        
    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            temp = temp.next
            list1 = list1.next
        else: 
            temp.next = list2
            temp = temp.next
            list2 = list2.next

    while list1:
        temp.next = list1
        temp = temp.next
        list1 = list1.next
    
    while list2:
        temp.next = list2
        temp = temp.next
        list2 = list2.next
    
    return result
    


def main():
    list1 = create_linked_list([2])
    list2 = create_linked_list([1])
    print(mergeTwoLists(list1,list2))

if __name__ == "__main__":
    main()