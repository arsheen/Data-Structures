# Shell sort
# Improvement over insertion sort
# Takes increments of list into consideration

def shell_sort(array):
    h = int(input("Enter the initial increment size:  "))
    while h >= 1:
        for i in range(h, len(array)):
            temp = array[i]
            j = i - h
            while j >= 0 and array[j] < temp:
                array[j+h] = array[j]
                j = j-h
            array[j+h] = temp
        h //= 2
    return array


def main():

    a = [0, 8, 1, 1, 9, 2, 5, 10, 10, 3, 7, 6, 4]

    shell = shell_sort(a)
    print("Shell Sort:          ", shell)

if __name__ == "__main__":
    main()