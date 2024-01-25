# Write a program that performs the sorting of an array using the mergesort strategy.


def mergesort(array,low,high):
    # This function divides the array into two parts and then call the merge function.
    mid = int((low+high)/2)
    if(low < high):
        mergesort(array=array,low=low,high=mid)
        mergesort(array=array,low=mid+1,high=high)
        merge(array=array,low=low,mid=mid,high=high)

def merge(array,low,mid,high):
    # This function merge the two subdivied array in a sorted order.
    n1 = mid - low + 1
    n2 = high - mid
    A1 = []
    A2 = []
    for x in range(n1):
        A1.append(array[low + x])
    for y in range(n2):
        A2.append(array[mid+y+1])
    i = j = 0
    k = low
    while(i < n1 and j < n2):
        if A1[i] < A2[j]:
            array[k] = A1[i]
            i += 1
        else:
            array[k] = A2[j]
            j += 1
        k += 1
    while(i < n1):
        array[k] = A1[i]
        i += 1
        k += 1
    while(j < n2):
        array[k] = A2[j]
        j += 1
        k += 1
# This sorting takes an average of O(nlogn) time for dividing and sorting the array. It also takes O(n) of space complexity for its implementation.

array = [9,8,1,4]
mergesort(array=array,low=0,high=3)
print(array)