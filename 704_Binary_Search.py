# 704. Binary Search

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        


def main():
    tests = [[[-1,0,3,5,9,12],9],[[-1,0,3,5,9,12],2],[[5],5]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.search(test[0],test[1])}")

if __name__ == "__main__":
    main()