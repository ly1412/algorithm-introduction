import math
arr = [44,33,2,55,78,9,1]

# sort arr[p to r]
def merge_sort(arr, p, r):
    print("Start ...")
    if (p < r):
        q = math.floor((p + r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, p+1, r)
        merge(arr, p, q, r)

# merge two parts of the arr one: arr[p to q],two: arr[q+1 to r] (p <= q < r)
def merge(arr, p, q, r):
    print("Merge start ...")
    n1 = q - p + 1
    n2 = r - q

    larr = []
    for i in range(p, q+1):
        larr.append(arr[i])

    rarr = []
    for i in range(q+1, r+1):
        rarr.append(arr[i])

    sarr = []
    i = 0
    j = 0

    for ind in range(0, n1 + n2):
        if i > n1-1:


if __name__ == '__main__':
    merge_sort(arr, 0, 7)
    print(arr)