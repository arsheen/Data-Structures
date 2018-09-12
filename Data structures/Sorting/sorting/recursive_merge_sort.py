#Requires an extra list to store n elements of array
#In place merge sort does exist but the run time is worse than that of the regular merge sort.
#In place merge sort is almost never used

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    return merge(left_list, right_list)

def merge(array1, array2):
    i = 0
    j = 0
    n1 = len(array1)
    n2 = len(array2)
    array_op = []


    while i < n1 and j < n2:
        if array1[i] < array2[j]:
            array_op.append(array1[i])
            i+=1

        elif array1[i] > array2[j]:
            array_op.append(array2[j])
            j+=1

        else:
            array_op.append(array1[i])
            array_op.append(array2[j])
            j+=1
            i+=1

    while i < n1:
        array_op.append(array1[i])
        i+=1

    while j < n2:
        array_op.append(array2[j])
        j+=1

    return array_op

def main():
    a = [1,6,3,6,6,8,2,5,2,3,3,6]
    print(merge_sort(a))

if __name__ == '__main__':
    main()
