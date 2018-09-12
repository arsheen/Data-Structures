# Improved bubble sort
# Takes care of the condition when the array is already sorted before the max. no. of passes are executed
# Data sensitive sort
# If data in sorted order         -> 1 pass, 0 swaps, n-1 comparison, O(n) complexity
# If data in reverse sorted order -> n-1 passes, n(n-1)/2 comparisons and swaps, O(n**2) complexity
# If data in random order         -> n-i comparisons for the ith pass
#                                 -> p passes = (2np - p**2 -p)/2 comparisons
#                                 -> O(n**2)

def bubble_v2(array):
    for i in range(len(array)-1, 0, -1):
        no_of_passes = 0
        for j in range(i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                no_of_passes += 1
        if no_of_passes == 0:
            break
    return array



def main():

    a = [0, 8, 1, 1, 9, 2, 5, 10, 10, 3, 7, 6, 4]
    bsv2 = bubble_v2(a)
    print("Bubble Sort improved:    ", bsv2)

if __name__ == "__main__":
    main()