# Fraction class
# Prof. O & CPTR-215
# 2023-10-02 constructor, repr, str
# 2023-10-04 

class Fraction:
    def __init__(self, numerator, denominator=1):
        """Create a fraction object.
        >>> Fraction(0)
        Fraction(0)
        >>> Fraction(1)
        Fraction(1)
        >>> Fraction(1, 2)
        Fraction(1, 2)
        """
        self.num = numerator
        self.den = denominator
    def __repr__(self) -> str:
        if self.den == 1:
            return f"Fraction({self.num})"
        else:
            return f"Fraction({self.num}, {self.den})"
    def __str__(self) -> str:
        return f"{self.num}/{self.den}"
    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        >>> Fraction(1, 2) + Fraction(1, 3)
        Fraction(5, 6)
        >>> Fraction(1, 2) + Fraction(1, 2) #TODO: Simplify in constructor
        Fraction(1)
        """
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)
    def __gt__(self, other):
        """
        >>> Fraction(1, 2) > Fraction(1, 3)
        True
        >>> Fraction(1, 3) > Fraction(1, 2)
        False
        """
        return self.num * other.den > other.num * self.den

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(Fraction(1, 2) > Fraction(1, 3))
    # Fraction(1, 2).__add__(Fraction(2, 3))
    # Fraction.__add__(Fraction(1, 2), Fraction(2, 3))