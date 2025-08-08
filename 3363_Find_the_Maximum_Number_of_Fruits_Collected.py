# 3363. Find the Maximum Number of Fruits Collected


class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits)
        dp: list[list[int]] = [[-1] * n for _ in range(n)]

        def count_child2_fruits(row, col, next_moves):
            dp[n - 1][n - 1] = 0
            for r in range(n - 1, 0, -1):
                for c in range(n - 1, r - 1, -1):
                    for nm in next_moves:
                        nr = r - nm[0]
                        nc = c - nm[1]
                        if not 0 <= nr < n > nc >= 0:
                            continue
                        if nr == nc:
                            dp[nr][nc] = 0
                            continue
                        dp[nr][nc] = max(dp[nr][nc], dp[r][c] + fruits[nr][nc])
            return dp[row][col]

        def count_child3_fruits(row, col, next_moves):
            dp[n - 1][n - 1] = 0
            for c in range(n - 1, 0, -1):
                for r in range(n - 1, c - 1, -1):
                    for nm in next_moves:
                        nr = r - nm[0]
                        nc = c - nm[1]
                        if not 0 <= nr < n > nc >= 0:
                            continue
                        if nr == nc:
                            dp[nr][nc] = 0
                            continue
                        dp[nr][nc] = max(dp[nr][nc], dp[r][c] + fruits[nr][nc])
            return dp[row][col]

        child1 = 0
        for i in range(n):
            child1 = child1 + fruits[i][i]

        child2_moves = [(1, -1), (1, 0), (1, 1)]
        child3_moves = [(-1, 1), (0, 1), (1, 1)]

        child2 = count_child2_fruits(0, n - 1, child2_moves)
        child3 = count_child3_fruits(n - 1, 0, child3_moves)

        max_fruits = child1 + child2 + child3
        return max_fruits


def main():
    tests = [
        [[8, 5, 0, 17, 15], [6, 0, 15, 6, 0], [7, 19, 16, 8, 18], [11, 3, 2, 12, 13], [17, 15, 15, 4, 6]],
        [[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]],
        [[1, 1], [1, 1]],
    ]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.maxCollectedFruits(test)}")


if __name__ == "__main__":
    main()
