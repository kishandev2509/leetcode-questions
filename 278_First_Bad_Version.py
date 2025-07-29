# 278. First Bad Version


class Solution:
    def __init__(self, bad_version) -> None:
        self.api_calls = 0
        self.bad_version = bad_version

    # The isBadVersion API is already defined for you.
    def isBadVersion(self, version: int) -> bool:
        self.api_calls += 1
        print(f"call isBadVersion({version})")
        return self.bad_version <= version

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        mid = left + (right - left) // 2
        while left < right:
            mid = left + (right - left) // 2
            # mid_bad = isBadVersion(mid)  # on leetcode
            mid_bad = self.isBadVersion(mid)
            if mid_bad:
                right = mid
            else:
                left = mid + 1
        # return left  # on leetcode
        return left
        
        

def main():
    tests = [[5, 4], [1, 1], [3, 2]]
    for test in tests:
        solution = Solution(test[1])
        print(f"{test} = {solution.firstBadVersion(test[0])}")


if __name__ == "__main__":
    main()
