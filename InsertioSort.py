def insertionn_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]#Current element to be compared key=a[j+1]
        j=i-1 #index of the previous element
        #move the element of array[0...i-1]that are greater than key ,.to one position ahead of their current position.
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key #swping or sorting value of key in to j+1
#Example usage.
arr=[12,13,5,6]
print("  UnSorted Array    :",arr)
print("=======================================================")
insertionn_sort(arr)
print ("Sorted array is:",arr)

        