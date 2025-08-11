# 118. Pascal's Triangle


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle


def main():
    tests = [5, 3, 1, 7]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.generate(test)}")


if __name__ == "__main__":
    main()
