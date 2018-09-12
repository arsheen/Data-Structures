# Insertion sort
# For each element considered, put it in the correct order with respect to the other elements

def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i-1
        while j >= 0 and array[j] < temp:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = temp
    return array

def main():

    a = [0, 8, 1, 1, 9, 2, 5, 10, 10, 3, 7, 6, 4]


    ins = insertion_sort(a)
    print("Insertion Sort:          ", ins)


if __name__ == "__main__":
    main()