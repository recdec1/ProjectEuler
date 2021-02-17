bohemoth = open("triangle.txt", "r")
bohemoth = (bohemoth.read()).split()
bohemoth = [int(x) for x in bohemoth]

bohePos = 0
matrix = []
lenBohem = 5050
for row in range(1, 101):
    list = []
    for i in range(bohePos, bohePos + row):
        list.append(bohemoth[i])
    for x in range(0, 100 - row):
        list.append(0)
    matrix.append(list)
    bohePos += row

def maxPathSum(tri, m, n):

    # loop for bottom-up calculation
    for i in range(m-1, -1, -1):
        for j in range(i+1):

            # for each element, check both
            # elements just below the number
            # and below right to the number
            # add the maximum of them to it
            if (tri[i+1][j] > tri[i+1][j+1]):
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i+1][j+1]

    # return the top element
    # which stores the maximum sum
    return tri[0][0]

print (maxPathSum(matrix, 99, 99))
