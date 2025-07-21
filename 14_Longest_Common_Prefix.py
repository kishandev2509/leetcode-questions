from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
        strs.sort(key=len)
        ans = strs[0]
        i = 1
        while i < len(strs):
            curr = strs[i]
            k = len(ans)
            while k>0 and curr[:k]!=ans:
                ans = ans[:-1]
                k = len(ans)
            i+=1
        return ans
        



def main():
    print(longestCommonPrefix(["flower","flow","flight"] ))

if __name__ == "__main__":
  main()