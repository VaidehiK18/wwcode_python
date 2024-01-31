## Write a program to find the maximum and minimum values in a list.
def min_max_singleLine(l):
    return max(l), min(l)

def min_max(l):
    min_value = max_value = l[0]
    for i in l:
        if i<min_value:
            min_value = i
        elif i>max_value:
            max_value = i
        else:
            pass
    return max_value,min_value

if __name__ == "__main__":
    list_len = int(input("Enter how many elements of the list?"))
    in_list = []
    for i in range(list_len):
        in_list.append(int(input()))
    print(f"The max and min of the list are {min_max_singleLine(in_list)} respectively")
    print(f"The max and min of the list are {min_max(in_list)} respectively")    