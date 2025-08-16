# 1323. Maximum 69 Number


class Solution:
    def maximum69Number(self, num: int) -> int:
        divisor = 1000
        return_num = 0
        while divisor >= 1:
            dividend = num // divisor
            if dividend == 6:
                return_num += 9 * divisor
                return_num += num % divisor
                return return_num
            else:
                return_num += dividend * divisor
            num %= divisor
            divisor //= 10
        return return_num


def main():
    tests = [9669, 9996, 9999]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.maximum69Number(test)}")


if __name__ == "__main__":
    main()
