from math import pi


class TCircle:
    def __init__(self, r=1.0):
        self.__r = r

    def get_radius(self):
        return self.__r

    def set_radius(self, value):
        if value >= 0:
            self.__r = value

    def s(self):
        return (self.__r ** 2) * pi

    def circuit(self):
        return 2 * pi * self.__r

    def __lt__(self, other):
        return self.__r < other.__r

    def __le__(self, other):
        return self.__r <= other.__r

    def __gt__(self, other):
        return self.__r > other.__r

    def __ge__(self, other):
        return self.__r >= other.__r

    def __eq__(self, other):
        return self.__r == other.__r

    def __ne__(self, other):
        return self.__r != other.__r

    def __add__(self, other):
        return TCircle(self.__r + other.__r)

    def __sub__(self, other):
        if self.__r - other.__r >= 0:
            return TCircle(self.__r - other.__r)
        else:
            return Exception("Radius must be >= 0")

    def __mul__(self, other):
        self.__r *= other


class TCylinder(TCircle):
    def __init__(self, r, h):
        super().__init__(r)
        self.__h = h

    def get_h(self):
        return self.__h

    def set_h(self, value):
        if value >= 0:
            self.__h = value

    def v(self):
        return (super().get_radius() ** 2) * pi * self.__h

    def s(self):
        return 2 * pi * super().get_radius() * self.__h

    def s_all(self):
        return 2 * pi * super().get_radius() * (self.__h + super().get_radius())

    def __lt__(self, other):
        return self.v() < other.v()

    def __le__(self, other):
        return self.v() <= other.v()

    def __gt__(self, other):
        return self.v() > other.v()

    def __ge__(self, other):
        return self.__r >= other.__r

    def __eq__(self, other):
        return self.v() == other.v()

    def __ne__(self, other):
        return self.v() != other.v()


radius = float(input("Radius : "))
h = float(input("H = "))
obj = TCylinder(radius,h)
print("V = ",obj.v())
print("S = ",obj.s())
new_h = float(input("New h = "))
obj.set_h(new_h)
print("V = ",obj.v())
print("S = ",obj.s())






