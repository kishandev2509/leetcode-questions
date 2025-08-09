# 231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


def main():
    tests = [1, 16, 3]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.isPowerOfTwo(test)}")


if __name__ == "__main__":
    main()
