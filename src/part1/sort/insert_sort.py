arr = [44,33,2,55,78,9,1]

def insert_sort():
    for i in range(1, len(arr)):
        print(i)
        take = arr[i]
        for j in range(0, i):
            j_revers = i -j -1
            if (arr[j_revers] > take):
                print(j_revers)
                arr[j_revers+1] = arr[j_revers]
                arr[j_revers] = take
        print("-----------------------")


if __name__ == '__main__':
    insert_sort()
    print(arr)