# 808. Soup Servings


from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0

        @lru_cache(None)
        def solve(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            prob = 0.25 * (solve(a - 100, b) + solve(a - 75, b - 25) + solve(a - 50, b - 50) + solve(a - 25, b - 75))
            return prob

        return solve(n, n)


def main():
    tests = [50, 100]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.soupServings(test)}")


if __name__ == "__main__":
    main()
