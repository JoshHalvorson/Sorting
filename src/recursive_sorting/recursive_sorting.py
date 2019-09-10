# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # TO-DO
    merged_arr = []
    # while the arrays are not empty, check if the value at the 0 index of one array
    # is smaller than the other, append that to the merged array and remove it from
    # the array it was in   
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    # if an array is empty, that means the other has some left over sorted value(s) in it
    # add it to the end of the merged array
    if len(arrA) == 0:
        merged_arr += arrB
    else:
        merged_arr += arrA
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    split1 = arr[len(arr) // 2:]
    split2 = arr[:len(arr) // 2]
    return merge(merge_sort(split1), merge_sort(split2))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
