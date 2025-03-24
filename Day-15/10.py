class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix  # List of lists

    def __getitem__(self, row):
        return self.matrix[row]

mat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[1])  # Output: [4, 5, 6]
