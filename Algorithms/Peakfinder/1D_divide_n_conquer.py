#find the peak by recursively dividing the array into half
def mid_index(start, end):
    return int((start + end)/2)


def peakfndr(array, i, j):
    mid = mid_index(i,j)
    if mid == 0:
        return mid
    elif array[mid-1] <= array[mid] >= array[mid+1]:
        return mid
    elif array[mid] < array[mid+1]:
        return peakfndr(array, mid+1, j)
    elif array[mid] < array[mid-1]:
        return peakfndr(array, i, mid-1)
    else:
        return "no peaks"



def main():
    end = "y"
    while(end != "n"):
        l = [int(x) for x in input("Enter a list with spaces between each number: ").split()]
        print(l)
        print(peakfndr(l, 0, (len(l)-1)))
        end = input("Continue? y/n: ")



if __name__ =="__main__":
    main()
