## Program to find the sum of all elements in a list
def findSum(in_list):
    s = 0
    in_list = [int(i) for i in in_list]
    for i in in_list:
        s+=i
    print(s)
    # This also gives the same result using inbuilt function
    print(sum(in_list))

if __name__ =="__main__":
    list_len = int(input("Enter how many elements of the list?"))
    in_list = []
    for i in range(list_len):
        in_list.append(input())
    findSum(in_list)
