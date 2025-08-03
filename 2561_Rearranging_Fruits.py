from collections import Counter
class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        cnt = Counter()
        for a, b in zip(basket1, basket2):
            cnt[a] += 1
            cnt[b] -= 1
        mi = min(cnt)
        nums = []
        for x, v in cnt.items():
            if v % 2:
                return -1
            nums.extend([x] * (abs(v) // 2))
        nums.sort()
        m = len(nums) // 2
        return sum(min(x, mi * 2) for x in nums[:m])
        


def main():
    tests = [[[2,3,4,1],[3,2,5,2]],[[4,2,2,2],[1,4,1,2]],[[2,3,4,1],[3,2,5,1]]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.minCost(test[0],test[1])}")

if __name__ == "__main__":
    main()