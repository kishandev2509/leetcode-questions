from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    visited = {}
    for i, num in enumerate(nums):
        counter = target - num
        if counter in visited:
            return [i,visited[counter]]
        visited[num]=i
    return []
    


def main():
    print(twoSum([2,7,11,15],9))

if __name__ == "__main__":
    main()