def lengthOfLongestSubstring(s: str) -> int:
    if s == "":
        return 0
    i,j=0,0
    res = 0
    ans = set()
    while i <= j < len(s):
        c = s[j] 
        while c in ans:
            ans.remove(s[i])
            i+=1
        else:
            ans.add(c)
            j+=1
        res = max(res,len(ans))
    return res


def main():
    tests = ["", " ", "pwwkew"]
    for test in tests:
        print(lengthOfLongestSubstring(test))

if __name__ == "__main__":
    main()