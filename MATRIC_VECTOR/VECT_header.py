import math

class Vector:
    """
    A class to represent a mathematical vector and perform vector operations.

    Attributes:
    -----------
    vect : list
        A list of numbers representing the vector components.

    Methods:
    --------
    __init__(self, vect=[]):
        Initializes the Vector object.

    __add__(self, other):
        Adds two vectors element-wise.

    __sub__(self, other):
        Subtracts two vectors element-wise.

    __matmul__(self, other):
        Computes the dot product of two vectors.

    magn(self):
        Computes the magnitude of the vector.

    normalize(self):
        Normalizes the vector to a unit vector.

    project_onto(self, other):
        Projects the vector onto another vector (not implemented).

    angle_with(self, other):
        Computes the angle between two vectors (not implemented).

    __repr__(self):
        Returns a string representation of the vector.
    """

    def __init__(self,vect=[]):
        """
        Initializes the Vector object.
        Parameters:
        -----------
        vect : list
        A list of numbers representing the vector components. Default is an empty list.

        """
        if not isinstance(vect, list):
            raise TypeError("Error: The provided argument is not a vector (list).")
        if not all(isinstance(x, (int, float)) for x in self.vect):
            ValueError("Both vectors must contain only numeric elements")
        self.vect = vect
    
    def __add__(self,other):
        """
        Adds two vectors element-wise.

        Parameters:
        -----------
        other : Vector
            Another vector to be added.

        Returns:
        --------
        Vector
            A new vector that is the element-wise sum of the two vectors.

        Raises:
        -------
        ValueError
            If the vectors are not of the same length.
        """

        if len(self.vect) != len(other.vect):
            raise ValueError("These vectors are not of the same length")
        else:
            sum_ = []
            for i in range(len(self.vect)):
                sum_.append(self.vect[i] + other.vect[i])
            return sum_
    def __sub__(self,other):
        """
        Subtracts two vectors element-wise.

        Parameters:
        -----------
        other : Vector
            Another vector to be subtracted.

        Returns:
        --------
        Vector
            A new vector that is the element-wise difference of the two vectors.

        Raises:
        -------
        ValueError
            If the vectors are not of the same length.
        """

        if len(self.vect) != len(other.vect):
            raise ValueError("These vectors are not of the same length")
        else:
            sum_ = []
            for i in range(len(self.vect)):
                sum_.append(self.vect[i] - other.vect[i])
            return sum_
    def __matmul__(self, other):
        """
        Computes the dot product of two vectors.

        Parameters:
        -----------
        other : Vector
            Another vector to compute the dot product with.

        Returns:
        --------
        float
            The dot product of the two vectors.

        Raises:
        -------
        ValueError
            If the vectors are not of the same length.
        """

        if len(self.vect) != len(other.vect):
            raise ValueError("These vectors are not of the same length")
        
        if not all(isinstance(x, (int, float)) for x in self.vect) or not all(isinstance(x, (int, float)) for x in other.vect):
            raise ValueError("Both vectors must contain only numeric elements")
        
        dot_product = sum(self.vect[i] * other.vect[i] for i in range(len(self.vect)))
        return dot_product
    
    def magn(self):
        """
        Computes the magnitude of the vector.

        Returns:
        --------
        float
            The magnitude of the vector.
        """
        return math.sqrt(sum(i**2 for i in self.vect))

    def normalize(self):
        """
        Normalizes the vector to a unit vector.

        Returns:
        --------
        Vector
            A new vector that is the normalized unit vector.

        Raises:
        -------
        ValueError
            If the vector is a zero vector.
        """
        magnitude = self.magn()
        if magnitude == 0:
            raise ValueError("Can't normalize a zero vector")
        normalized_vect = [(i / magnitude) for i in self.vect]
        return Vector(normalized_vect)

    def project_onto(self,other):
        """
        Projects the vector onto another vector.

        Parameters:
        -----------
        other : Vector
            The vector to project onto.
        """
        pass

    def angle_with(self,other):

        """
        Computes the angle between two vectors.

        Parameters:
        -----------
        other : Vector
            The vector to compute the angle with.
        """
        theta = math.acos((self @ other)/(self.magn() * other.magn()))
        return theta


    def __repr__(self):
        """
        Returns a string representation of the vector.

        Returns:
        --------
        str
            A string representation of the vector.
        """
        return f"Vector({self.vect})"


x=Vector([4, 5,6])
y = Vector([4, 5,6])

print(x.angle_with(y))