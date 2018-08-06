#consider a 2D matrix of numbers. Here, a peak is defined as:
#  "a number which is larger than the numbers at its four edges"
#Brute force method goes through every element of every row and coulmn

def peakfndr(matrix):
    max_val = []
    for i in matrix:
        max_val = {max(i): [matrix.index(i),i.index(max(i))]}

    return [max(max_val),max_val[max(max_val)]]




def main():
    end = "y"
    while(end != "n"):
        matrix = []
        rows = int(input("Enter the no. of rows of matrix: "))
        #cols = int(input("Enter the no. of cols of matrix: "))
        for i in range(rows):
            l = [int(x) for x in input("Enter row {} with a space between each number: ".format(i)).split()]
            print(l)
            matrix.append(l)
        #print(matrix)
        print(peakfndr(matrix))
        end = input("Continue? y/n: ")


if __name__ =="__main__":
    main()

