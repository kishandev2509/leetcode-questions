# 342. Power of Four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
        


def main():
    tests = [16,5,1,64]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.isPowerOfFour(test)}")

if __name__ == "__main__":
    main()