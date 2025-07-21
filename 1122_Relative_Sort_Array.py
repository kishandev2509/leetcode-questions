from typing import List
from collections import defaultdict

# def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
#     def get_index(i,arr):
#         try:
#             return arr.index(i)
#         except ValueError:
#             return len(arr)+i
#     arr1.sort(key= lambda x: get_index(x,arr2))
#     return arr1
    
def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    count = defaultdict(int)
    remainning = []
    for num in arr1:
        if num in arr2:
            count[num]+=1
        else:
            remainning.append(num)
    ans = []
    for num in arr2:
        ans.extend([num]*count[num])
    return ans+sorted(remainning)


def main():
    tests = [([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]),([28,6,22,8,44,17],[22,28,8,6])]
    for test in tests:
        print(relativeSortArray(test[0],test[1]))

if __name__ == "__main__":
    main()