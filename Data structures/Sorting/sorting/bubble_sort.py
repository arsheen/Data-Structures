# bubble sort
# inplace sorting
# Unstable Sort
# Compare every two elements and swap them if the element on the right is larger than the one on the left


def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def main():

    a = [0, 8, 1, 1, 9, 2, 5, 10, 10, 3, 7, 6, 4]


    bs = bubble_sort(a)
    print("Bubble Sort:             ", bs)


if __name__ == "__main__":
    main()