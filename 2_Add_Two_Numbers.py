from ListNodeModule import ListNode, create_list


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
    result = None
    curr = None
    num1 = l1
    num2 = l2
    carry = 0
    
    while num1 is not None or num2 is not None or carry !=0:
        total_sum = carry
        
        if num1 is not None:
            total_sum += num1.val
            num1 = num1.next
            
        if num2 is not None:
            total_sum += num2.val
            num2 = num2.next
            
        new_node = ListNode(val = total_sum %  10)
        carry = total_sum // 10
        
        if curr is None:
            result = new_node
            curr = result
        else:
            curr.next = new_node
            curr = curr.next
            
    return result



def main():
    l1 = create_list([2,4,3])
    l2 = create_list([0,0,9])
    print(addTwoNumbers(l1,l2))

if __name__ == "__main__":
    main()