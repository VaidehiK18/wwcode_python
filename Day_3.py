## Program to count vowels in a string
def count_vowels(string):
    string = string.lower()
    vowels = ['a','e','i','o','u']
    cnt = 0
    for i in string:
        x = i in vowels
        if i in vowels:
            cnt+=1
    return cnt

if __name__ == "__main__":
    string = input()
    print(count_vowels(string))
