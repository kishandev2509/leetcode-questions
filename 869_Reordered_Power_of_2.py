# 869. Reordered Power of 2
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digit(n: int) -> list[int]:
            digits = [0] * 10
            while n > 0:
                digits[n % 10] += 1
                n //= 10
            return digits

        input = count_digit(n)
        for i in range(31):
            if input == count_digit(1 << i):
                return True
        return False



def main():
    tests = [1,10,821,125,126]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.reorderedPowerOf2(test)}")

if __name__ == "__main__":
    main()