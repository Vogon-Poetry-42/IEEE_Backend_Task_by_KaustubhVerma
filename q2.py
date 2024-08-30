###         IEEE Backend task 2           ###
### by Kaustubh Verma, EEE, 2024A3PS0645P ###


def spiral(n):
    matrix = [[0 for j in range(n)] for i in range(n)]

    boundaryR = n-1
    boundaryL = 0
    boundaryU = 1
    boundaryD = n-1
    move = "r" # right -> r; down -> d; left -> l; up -> u
    row, col = 0, 0
    
    for i in range(1, n**2 + 1):
        matrix[row][col] = i

        if (move == "r"):
            col += 1
        elif (move == "d"):
            row += 1
        elif (move == "l"):
            col -= 1
        elif (move == "u"):
            row -= 1

        if (col == boundaryR and move == "r"):
            move = "d"
            boundaryR -= 1
        elif (row == boundaryD and move == "d"):
            move = "l"
            boundaryD -= 1
        elif (col == boundaryL and move == "l"):
            move = "u"
            boundaryL += 1
        elif (row == boundaryU and move == "u"):
            move = "r"
            boundaryU += 1

    return matrix
        



def main():

    n = int(input())

    returned_matrix = spiral(n)

    for i in range(n):
        for j in range(n):
            print(returned_matrix[i][j], end = "\t")
        print()
    



if __name__ == "__main__":
    main()
