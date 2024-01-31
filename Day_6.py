## Write a program to count the occurrences of a specific character in a string.
def count_singleLine(s,c):
    return s.count(c)

def count_occurrences(s,c):
    cnt = 0
    for i in s:
        if i == c:
            cnt+=1
    return cnt

if __name__ == "__main__":
    s = input("Enter the string-")
    c = input("Enter the character you want to count-")
    print(f"{c} occurs {count_singleLine(s,c)} times in {s}")
    print(f"{c} occurs {count_occurrences(s,c)} times in {s}")