# 904. Fruit Into Baskets


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruit_types = {}
        total_fruits_in_basket, max_fruits = 0, 0
        left, right = 0, 0
        while right < len(fruits):
            if fruits[right] not in fruit_types:
                fruit_types[fruits[right]] = 1
                total_fruits_in_basket += 1
            else:
                fruit_types[fruits[right]] += 1
            right += 1
            while total_fruits_in_basket > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    fruit_types.pop(fruits[left])
                    total_fruits_in_basket -= 1
                left += 1
            max_fruits = max(max_fruits, right - left)
        return max_fruits


def main():
    tests = [[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], [1, 2, 1], [0, 1, 2, 2], [1, 2, 3, 2, 2]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.totalFruit(test)}")


if __name__ == "__main__":
    main()
