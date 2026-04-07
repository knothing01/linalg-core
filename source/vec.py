import numpy as np
import numbers

class Vector:
    def __init__(self, data):
        self._data = tuple(data)
        self._dim = len(data)

    def __len__(self):
        return self._dim

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"index must be int, not {type(index).__name__}")

        if index >= self._dim:
            raise IndexError(f"index {index} out of range for length {self._dim}")

        return self._data[index]


    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if len(other) != self._dim:
            raise ValueError(f"dimension mismatch: {self._dim} vs {len(other)}")

        summed = []
        for idx in range(self._dim):
            summed.append(self._data[idx] + other[idx])

        return Vector(summed)


    def _scaled_components(self, scalar):
        if not isinstance(scalar, numbers.Number):
            raise TypeError("scalar must be a number")

        scaled = []
        for idx in range(self._dim):
            scaled.append(self._data[idx] * scalar)

        return tuple(scaled)


    def scalarMult(self, scalar):
        self._data = self._scaled_components(scalar)
        return self


    def __mul__(self, scalar):
        return Vector(self._scaled_components(scalar))


    def __rmul__(self, scalar):
        return Vector(self._scaled_components(scalar))


    def __radd__(self, other):
        if other == 0:
            return self

        return self.__add__(other)

    def dot(self, other) -> float:
        if not isinstance(other, Vector):
            raise TypeError("they must be the same type")
        
        if len(other) != self._dim:
            raise ValueError(f"dimension mismatch: {self._dim} vs {len(other)}")
        
        dotPrd = 0 

        for idx in range(self._dim):
            dotPrd += self._data[idx] * other[idx]
        
        return dotPrd

    def printVector(self):
        print(self._data)

if __name__ == "__main__":
    a = Vector((1, 2, 3, 4, 5))
    b = Vector((1,2,3,4,63))
    g = Vector((4,7,6,5,45))
    c = a + b + g
    # c.scalarMult(0)
    # b = 5 * a
    print(a.dot(b))
    b.printVector()
