import math
import sys

arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

def find_max_sub_arr(arr, low, high):
    # print("low:", low)
    # print("high:", high)
    if high == low:
        return (low, high, arr[low])
    else:
        mid = math.floor((low + high)/2)
        (left_low, left_high, left_sum) = find_max_sub_arr(arr, low, mid)
        (right_low, right_high, right_sum) = find_max_sub_arr(arr, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_sub_arr(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= cross_sum and right_sum >= left_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def find_max_crossing_sub_arr(arr, low, mid, high):
    left_sum = -sys.maxsize - 1
    max_ind_left = 0

    sum = 0
    for i in range(mid, low-1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_ind_left = i

    sum = 0
    right_sum = -sys.maxsize - 1
    max_ind_right = 0
    for i in range(mid+1, high):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            max_ind_right = i
    
    return (max_ind_left, max_ind_right, left_sum + right_sum)

if __name__ == '__main__':
    (lowInd, highInd, sum) = find_max_sub_arr(arr, 0, len(arr)-1)
    print("lowInd:", lowInd)
    print("highInd:", highInd)
    print("sum:", sum)