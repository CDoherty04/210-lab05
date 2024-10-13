"""
Name: Charlie Doherty
KUID: 3115329
EECS 210 Lab Session: Thursday 4-6
Lab: 06
Description: Program that takes a number and produces the next num in lexicographic order
Collaborators: None
"""


def next_permutation(num):
    n = len(num) - 1
    j = n - 1
    # While aj > aj+1
    while int(num[j]) > int(num[j + 1]):
        j -= 1
    k = n
    # While aj > ak
    # ak will always be smaller than aj
    while int(num[j]) > int(num[k]):
        k -= 1
    # Interchange aj and ak
    # Concatenate the string from the smallest index, replacing the bigger value...
    # ...to the largest index replacing the smaller value, and add back rest of string if possible
    if (max(j, k) + 1) > n:
        num = num[:min(j, k)] + num[max(j, k)] + num[min(j, k) + 1:max(j, k)] + num[min(j, k)]
    else:
        num = num[:min(j, k)] + num[max(j, k)] + num[min(j, k) + 1:max(j, k)] + num[min(j, k)] + num[max(j, k) + 1]
    r = n
    s = j + 1
    while r > s:
        # interchange ar and as with same process
        if (max(r, s) + 1) > n:
            num = num[:min(r, s)] + num[max(r, s)] + num[min(r, s) + 1:max(r, s)] + num[min(r, s)]
        else:
            num = num[:min(r, s)] + num[max(r, s)] + num[min(r, s) + 1:max(r, s)] + num[min(r, s)] + num[max(r, s) + 1]
        r -= 1
        s += 1
    # return the next permutation
    return num


def get_num():
    return input("Enter a string of numbers:\n")


# Main function that gets input, processes, and outputs
if __name__ == "__main__":
    user_num = get_num()
    np = next_permutation(user_num)
    print(f"The next permutation of {user_num} is {np}")
