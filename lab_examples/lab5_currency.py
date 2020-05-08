from numbers import Number

class Dollar:

    def __init__(self, value=1.0):
        self.value = value

    def __repr__(self):
        base = '<{:.2f} dollar{}>'
        return base.format(self.value, 's' if self.value != 1 else '')

    def __add__(self, other):   # Same as my_dollar + other

        if isinstance(other, Dollar):
            return Dollar(self.value + other.value)

        if isinstance(other, Yen):
            return Dollar(self.value + other.value / 106.5)

        elif isinstance(other, Number):
            return Dollar(self.value + other)

        else:
            raise TypeError('Cannot add Dollar with object of type {}!'.format(type(other).__name__))

    def __radd__(self, other):
        if isinstance(other, Yen):
            return Yen(self.value * 106.5 + other.value)
        elif isinstance(other, Number):
            return Dollar(other + self.value)
        else:
            raise TypeError


class Yen:
    def __init__(self, value=1.0):
        self.value = value

    def __repr__(self):
        base = '<{:.0f} yen>'
        return base.format(self.value)


if __name__ == '__main__':
    us_wallet = Dollar(5.319)
    jpn_wallet = Yen(5310)

    print(us_wallet)
    print(us_wallet + 5)
    print(5 + us_wallet)

    print(us_wallet + jpn_wallet)
    print(jpn_wallet + us_wallet)