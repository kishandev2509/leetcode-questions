# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


class Solution:
    number = 0
    def __init__(self, num) -> None:
        self.number = num

    def guess(self, num: int) -> int:
        return -1 if num > self.number else 1 if num < self.number else 0

    def guessNumber(self, n: int) -> int:
        min, max = 0, n
        guessed = min + (max - min) // 2
        while (gues := self.guess(guessed)) != 0:
            if gues == 0:
                return n
            elif gues == -1:
                max = guessed
            else:
                min = guessed + 1
            guessed = min + (max - min) // 2
        return guessed
        



def main():
    tests = [[10,6],[1,1],[2,1]]
    for test in tests:
        solution = Solution(test[1])
        print(f"{test} = {solution.guessNumber(test[0])}")

if __name__ == "__main__":
    main()
