class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1_000_000_007
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def find_ways(rem: int, cur: int, pow: int, memo: list[list[int]]) -> int:
            if rem == 0:
                return 1
            if rem < 1:
                return 0
            num = cur**pow
            if num > n:
                return 0
            if memo[rem][cur] != -1:
                return memo[rem][cur]
            pick = find_ways(rem - num, cur + 1, pow, memo) % MOD
            not_pick = find_ways(rem, cur + 1, pow, memo) % MOD
            memo[rem][cur] = (pick + not_pick) % MOD
            return memo[rem][cur]

        return find_ways(n, 1, x, memo)


def main():
    tests = [[10, 2], [4, 1], [64, 1]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.numberOfWays(test[0], test[1])}")


if __name__ == "__main__":
    main()
