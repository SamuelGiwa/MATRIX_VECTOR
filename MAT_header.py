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
                    self.temp[i][j] += self.data[k][j]*other.data[i][k]

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

        self.data = array

    def addMat(self, other):
        pass

# Example usage
matrix1 = Matrix(2, 2)  # Create a 2x2 matrix
matrix2 = Matrix(2, 2)

matrix1.matProduct(matrix2)
z = matrix1.temp
print(z)