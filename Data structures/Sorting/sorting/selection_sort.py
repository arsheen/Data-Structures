# selection sort
# Inplace sorting
# Unstable Sort
# check for the smallest element in the array and place it in the smallest index possible
# n passes and n-1 swaps
# n(n-1)/2 total swaps
# O(n**2) complexity


def selection_sort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[minIndex] < array[j]:
                minIndex = j
        if i != minIndex:
            array[minIndex], array[i] = array[i], array[minIndex]
    return array

def main():

    a = [0, 8, 1, 1, 9, 2, 5, 10, 10, 3, 7, 6, 4]


    ss = selection_sort(a)
    print("Selection Sort:          ", ss)

if __name__ == "__main__":
    main()