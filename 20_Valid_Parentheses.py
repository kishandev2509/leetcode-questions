def isValid(s: str) -> bool:
    parans = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
    visited =[]
    for paran in s:
        if paran in parans and len(visited) > 0 and visited[-1] == parans[paran]:
            visited.pop()
        else:
            visited.append(paran)
    return len(visited) == 0
        



def main():
    print(isValid("]"))

if __name__ == "__main__":
  main()