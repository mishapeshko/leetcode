class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        large = 2**31
        larger = large*2
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if i != 0 and j != 0:
                        if matrix[i][0] != 0 and matrix[i][0] != larger:
                            matrix[i][0] = large
                        else:
                            matrix[i][0] = larger
                        if matrix[0][j] != 0 and matrix[0][j] != larger:
                            matrix[0][j] = large
                        else:
                            matrix[0][j] = larger
                    else:
                        matrix[i][j] = larger
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == large or matrix[0][j] == large or matrix[i][0] == larger or matrix[0][j] == larger:
                    matrix[i][j] = 0
        frhz = 0
        for j in range(cols):
            if matrix[0][j] == larger:
                frhz = 1
            if matrix[0][j] == large:
                matrix[0][j] = 0
        fchz = 0
        for i in range(rows):
            if matrix[i][0] == larger:
                fchz = 1
            if matrix[i][0] == large:
                matrix[i][0] = 0
        if frhz == 1:
            for j in range(cols):
                matrix[0][j] = 0
        if fchz == 1:
            for i in range(rows):
                matrix[i][0] = 0

# of course the solution is in-place
