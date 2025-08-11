class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        powers = []
        for i in range(32):
            if n & (1 << i) != 0:
                powers.append(1 << i)
        max_prod = 1000000007
        ans = []
        for i, j in queries:
            product = 1
            for k in range(i, j + 1):
                product = ((product % max_prod) * (powers[k] % max_prod)) % max_prod
            ans.append(product)
        return ans


def main():
    tests = [[15, [[0, 1], [2, 2], [0, 3]]], [2, [[0, 0]]]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.productQueries(test[0], test[1])}")


if __name__ == "__main__":
    main()
