class Matrix:
    def __init__(self, row: int,col: int):
        self.row = row
        self.col = col
        self.data = []  # Initialize an empty list to store matrix data
        self.createMatrix()
        self.temp = []

    def createMatrix(self):
        print("Enter the values for the matrix:")
        for i in range(self.row):
            row_data = []
            for j in range(self.col):
                value = int(input(f"Enter value [{i}][{j}]: "))
                row_data.append(value)
            self.data.append(row_data)
        print("Matrix created successfully!")

    def display(self):
        for row in self.data:
            print(row)

    def matProduct(self, other):

        if self.row != self.column:
            print("Matrix multiplication not possible; dimension mismatch")
            return
        result = [[0 for _ in range(self.row)] for _ in range(self.column)]


        for i in range(self.row):
            for j in range(self.col):
                for k in range(self.col):
                    result[i][j] += self.data[k][j]*other.data[i][k]
        return result

    def matAdd(self,other):
        rows, cols = self.row, other.col
        array = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            array.append(row)
        self.temp = array

        for i in range(self.row):
            for j in range(self.col):
                for k in range(self.col):
                    self.temp[i][j] = self.data[i][k]+other.data[i][k]

    def matSub(self,other):
        rows, cols = self.row, other.col
        array = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            array.append(row)
        self.temp = array

        for i in range(self.row):
            for j in range(self.col):
                for k in range(self.col):
                    self.temp[i][j] = self.data[i][k]-other.data[i][k]

                

    def transpose(self):
        rows, cols = self.row, self.col
        array = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            array.append(row)
        self.temp = array

        for i in range(rows):
            for j in range(cols):
                array[i][j] = self.data[j][i]

        return array
    
    def determinant(self):
        if self.row != self.col:
            print("Determinant is only defined for symmetrical matrix")
            return

        def _determinant(matrix):
            # Base case for 2x2 matrix
            if len(matrix) == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

            # Recursive case for larger matrices
            determinant = 0
            for c in range(len(matrix)):
                minor = [row[:c] + row[c+1:] for row in (matrix[:0] + matrix[1:])]
                determinant += ((-1)**c) * matrix[0][c] * _determinant(minor)
            return determinant

        return _determinant(self.data)