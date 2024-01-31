## Write a program to check if a number is positive, negative, or zero.
def check(n):
    if n == 0:
        return "Zero"
    elif n>0:
        return "Positive"
    else:
        return "Negative"

if __name__ == "__main__":
    n = int(input())
    print(f" The given number is {check(n)}")