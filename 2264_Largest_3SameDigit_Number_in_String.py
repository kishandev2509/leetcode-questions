class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            triple_digit_str = str(digit) * 3
            if triple_digit_str in num:
                return triple_digit_str
        return ""


def main():
    tests = ["1221000", "222", "6777133339", "2300019", "42352338"]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.largestGoodInteger(test)}")


if __name__ == "__main__":
    main()
