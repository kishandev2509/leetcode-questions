# 817. Linked List Components
from ListNodeModule import ListNode,create_linked_list


class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        ans = 0
        numsSet = set(nums)
        while head:
            if head.val in numsSet and (head.next is None or head.next.val not in numsSet):
                ans += 1
            head = head.next
        return ans




def main():
    tests = [[[0,1,2,3],[0,1,3]],[[0,1,2,3,4],[0,3,1,4]]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.numComponents(create_linked_list(test[0]),test[1])}")

if __name__ == "__main__":
    main()