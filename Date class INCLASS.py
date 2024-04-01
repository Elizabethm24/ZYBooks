# Date class
# Prof. O & CPTR-215
# 2023-09-27 __init__ & is_in_leap_year
# 2023-09-29 doctests & ...

class Date:
    def __init__(self, year: int, month: int, day: int):
        """Initialize a date with year, month, and day.
        >>> Date(2023, 9, 29).year
        2023
        >>> tomorrow = Date(2023, 9, 30)
        >>> tomorrow.day
        30
        >>> Date(2023, 10, 1)
        Date(2023, 10, 1)
        """
        self.year = year
        self.month = month
        self.day = day
    def __repr__(self) -> str:
        return f"Date({self.year}, {self.month}, {self.day})"
    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day}"
    def is_in_leap_year(self):
        return self.year % 4 == 0
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    today = Date(2023, 9, 27)
    print(today.is_in_leap_year())