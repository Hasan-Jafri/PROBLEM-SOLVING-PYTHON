# Write a program that performs the sorting of an array using the quicksort strategy.


def QuickSort(array,low,high):
    if(low < high):
        pi = partition(array=array,low=low,high=high)
        QuickSort(array=array,low=low,high=pi-1)
        QuickSort(array=array,low=pi+1,high=high)

def partition(array,low,high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] < pivot:
            i += 1
            (array[i] , array[j] )= (array[j], array[i])
            
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i + 1

array = [9,8,4,1,3,7,9,6,99]
QuickSort(array=array,low=0,high=3)
print(array)