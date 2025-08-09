# 231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0


def main():
    tests = [1, 16, 3]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.isPowerOfTwo(test)}")


if __name__ == "__main__":
    main()
