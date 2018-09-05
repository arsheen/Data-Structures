#find ANY peak in the given 1D array
def peak_finder(array):
    for i in range(len(array)):
        if array[i-1]<=array[i]>=array[i+1]:
            return i
    return "No peaks"

def main():
    end = "y"
    while(end != "n"):
        l = [int(x) for x in input("Enter a list with spaces between each number: ").split()]
        print(l)
        print(peak_finder(l))
        end = input("Continue? y/n: ")

if __name__ =="__main__":
    main()
