class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        j = 0
        for i in range((n+1)//2):
            changeLayer(matrix, j, n)
            j += 1

def changeLayer(matrix, start, n):
    for i in range(start, n-1-start):
        first = matrix[start][i]
        second = matrix[i][n-1-start]
        third = matrix[n-1-start][n-1-i]
        fourth = matrix[n-1-i][start]
        matrix[start][i] = fourth
        matrix[i][n-1-start] = first
        matrix[n-1-start][n-1-i] = second
        matrix[n-1-i][start] = third
