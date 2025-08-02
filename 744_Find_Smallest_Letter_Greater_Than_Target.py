# 744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:
            return letters[0]
        left, right = 0, len(letters)-1
        while left < right:
            mid = left + (right - left)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left]
        


def main():
    tests = [[["e","e","e","e","e","e","n","n","n","n"],"e"],[["c","f","j"],"a"],[["c","f","j"],"c"],[["x","x","y","y"],"z"],[["c","f","j"],"d"]]
    for test in tests:
        solution = Solution()
        print(f"{test} = {solution.nextGreatestLetter(test[0],test[1])}")

if __name__ == "__main__":
    main()