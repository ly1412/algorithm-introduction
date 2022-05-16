import math
arr = [44,33,2,55,78,9,1]

# sort arr[p to r]
def merge_sort(arr, p, r):
    print("Start ...")
    if (p < r):
        q = math.floor((p + r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

# merge two parts of the arr one: arr[p to q],two: arr[q+1 to r] (p <= q < r)
def merge(arr, p, q, r):
    print("Merge start ...")
    print("p:", p)
    print("q:", q)
    print("r:", r)
    n1 = q - p + 1
    n2 = r - q

    larr = []
    for i in range(p, q+1):
        larr.append(arr[i])

    print("larr:", larr)

    rarr = []
    for i in range(q+1, r+1):
        rarr.append(arr[i])

    print("rarr:", rarr)

    i = 0
    j = 0

    for ind in range(p, r+1):
        if i <= n1-1 and j <= n2 -1:
            if larr[i] < rarr[j]:
                arr[ind] = larr[i]
                i += 1
            else:
                arr[ind] = rarr[j]
                j += 1
        elif i > n1-1:
            arr[ind] = rarr[j]
            j += 1
        elif j > n2-1:
            arr[ind] = larr[i]
            i += 1

if __name__ == '__main__':
    merge_sort(arr, 0, 6)
    print(arr)