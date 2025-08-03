# 27. Remove Element


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            while nums[right] == val and right > left:
                right -= 1
            if left == right and nums[left] == val:
                return left
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
        return left


def main():
    tests = [[[3, 2, 2, 3], 3], [[0, 1, 2, 2, 3, 0, 4, 2], 2], [[3, 3, 3, 3], 3], [[2], 3]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.removeElement(test[0], test[1])}")


if __name__ == "__main__":
    main()
