# 2106. Maximum Fruits Harvested After at Most K Steps


class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        max_fruits = window_start = total_fruits = 0
        for window_end, (position_j, fruits_at_j) in enumerate(fruits):
            total_fruits += fruits_at_j
            while (
                window_start <= window_end
                and position_j
                - fruits[window_start][0]
                + min(abs(startPos - fruits[window_start][0]), abs(startPos - position_j))
                > k
            ):
                total_fruits -= fruits[window_start][1]
                window_start += 1
            max_fruits = max(max_fruits, total_fruits)
        return max_fruits



def main():
    tests = [[[[2,8],[6,3],[8,6]],5,4],[[[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]],5,4],[[[0,3],[6,4],[8,5]],3,2]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.maxTotalFruits(test[0],test[1],test[2])}")

if __name__ == "__main__":
    main()