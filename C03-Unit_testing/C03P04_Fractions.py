class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.

        If denominator = 0, raise ValueError.
        """
        if denominator == 0:
            raise ValueError('denominator must be greater than 0')

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """
        Returns the string representation of self.
        """
        return f'{self.numerator} / {self.denominator}'

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        if self.numerator == 0:
            return f'{self.numerator}'

        return f'{self.numerator} / {self.denominator}'

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator

        return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator / self.denominator < other.numerator / other.denominator

        raise TypeError("Can't compare instances of different classes")

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if isinstance(other, Fraction):
            if self.denominator == other.denominator:
                new_numerator = self.numerator + other.numerator
                return Fraction(new_numerator, self.denominator)

            new_numerator = (other.denominator * self.numerator) + (self.denominator * other.numerator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)

        raise TypeError('You can only add objects from same class')

    def __sub__(self, other):
        """
        Returns new Fraction, that's the substraction of self and other.
        """
        if isinstance(other, Fraction):
            if self.denominator == other.denominator:
                new_numerator = self.numerator - other.numerator
                return Fraction(new_numerator, self.denominator)

            new_numerator = (other.denominator * self.numerator) - (self.denominator * other.numerator)
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)

        raise TypeError('You can only subtract objects from same class')

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)

        raise TypeError('You can only multiply objects from same class')

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        new_numerator = self.numerator // self.euclid_gcd()
        new_denominator = self.denominator // self.euclid_gcd()
        return Fraction(new_numerator, new_denominator)

    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
        return self.numerator == self.numerator // self.euclid_gcd()

    def euclid_gcd(self):
        num1 = self.numerator
        num2 = self.denominator

        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        return num1
