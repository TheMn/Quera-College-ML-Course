class Complex:

    def __init__(self, real, img):
        self._real = real
        self._img = img

    def set_real(self, real):
        self._real = float(real)

    def get_real(self):
        return float(self._real)

    def __str__(self):
        return "{r:.2f} {s} {i:.2f}i".format(r=self._real, s="+" if self._img >= 0 else "-",
                                             i=self._img if self._img >= 0 else -self._img)


c = Complex(2, 0)
print(c.__str__())
