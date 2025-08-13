class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        return 1162261467 % n == 0



def main():
    tests = [27,0,-1,2187]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.isPowerOfThree(test)}")

if __name__ == "__main__":
    main()