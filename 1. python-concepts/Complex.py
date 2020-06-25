from math import sqrt


class Complex:

    def __init__(self, real=0.0, img=0.0):
        self._real = float(real)
        self._img = float(img)

    @classmethod
    def from_string(cls, s: str):
        if '+' in s:
            try:
                u_real, u_img = s.split('+')
                u_real = float(u_real.strip())
                u_img = float(u_img.strip()[:-1])
                return cls(u_real, u_img)
            except Exception:
                raise ValueError("Wrong Format")
        elif '-' in s:
            try:
                u_real, u_img = s.split('-')
                u_real = float(u_real.strip())
                u_img = float(u_img.strip()[:-1])
                return cls(u_real, -1 * u_img)
            except Exception:
                raise ValueError("Wrong Format")
        else:
            raise ValueError("Wrong Format")

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = float(value)

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = float(value)

    def __str__(self):
        if self._img < 0:
            return "{0:.2f} - {1:.2f}i".format(self._real, -1 * self._img)
        elif self._img > 0:
            return "{0:.2f} + {1:.2f}i".format(self._real, self._img)
        else:
            return "{0:.2f}".format(self._real)

    @property
    def magnitude(self):
        return sqrt(self._real ** 2 + self._img ** 2)

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise TypeError
        else:
            return Complex(self._real + other.real, self._img + other.img)

    def __sub__(self, other):
        if not isinstance(other, Complex):
            raise TypeError
        else:
            return Complex(self._real - other.real, self._img - other.img)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise TypeError
        else:
            return Complex(self._real * other.real - self._img * other.img,
                           self._real * other.img + self._img * other.real)
