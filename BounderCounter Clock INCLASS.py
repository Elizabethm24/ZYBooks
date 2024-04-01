# Bounded Counters
# Prof. O & CPTR-215
# 2023-10-04 wrote & tested constructor, repr, str, increment, reset
# 2023-10-06
# 2023-10-20 add 12-hour clock (class Clock12)
# 2023-10-25 

class BoundedCounter:
    def __init__(self, lowerBound = 0, upperBound = 9,
                 neighbor = None, startValue = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.currentValue = lowerBound if startValue is None else startValue
        self.neighbor = neighbor
    def __repr__(self):
        return f"BoundedCounter({self.lowerBound}, {self.upperBound}, {self.neighbor!r})"
    def __str__(self):
        return f"{'' if self.neighbor is None else self.neighbor}{self.currentValue}"
    def increment(self):
        """
        >>> bit = BoundedCounter(0, 1)
        >>> print(bit)
        0
        >>> bit.increment()
        >>> print(bit)
        1
        >>> bit.increment()
        >>> print(bit)
        0
        """
        self.currentValue += 1
        if self.currentValue > self.upperBound:
            self.reset()
            if self.neighbor:
                self.neighbor.increment()
            
    def reset(self):
        self.currentValue = self.lowerBound
    def get(self):
        return self.currentValue
    
class ListCounter():
    def __init__(self, items : list, neighbor = None, startValue = None):
        self.items = items
        self.index = BoundedCounter(0, len(items) - 1, neighbor, \
                                    items.index(startValue) if startValue is not None else 0)
        self.neighbor = neighbor
    def __str__(self):
        return ("" if self.neighbor is None else str(self.neighbor)) + \
               str(self.get())
    def increment(self):
        self.index.increment()
    def get(self):
        return self.items[self.index.get()]

class Clock12:
    def __init__(self, hours = 12, minutes = 0, ampm="AM"):
        """
        >>> Clock12()
        Clock12(12, 0, 'AM')
        >>> Clock12(10, 0, 'am')
        Clock12(10, 0, 'AM')
        >>> print(Clock12(10, 13, 'am'))
        AM 10:13
        """
        self.ampm = ListCounter(["AM", "PM"], None, ampm.upper())
        space = ListCounter([' '], self.ampm)
        self.hours = ListCounter([12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], space, hours)
        colon = ListCounter([':'], self.hours)
        self.minutes_tens = BoundedCounter(0, 5, colon, minutes // 10)
        self.minutes_ones = BoundedCounter(0, 9, self.minutes_tens, minutes % 10)
    def __repr__(self):
        return f"Clock12({self.hours.get()}, {self.minutes_tens.get() * 10 + self.minutes_ones.get()}, '{self.ampm}')"
    def __str__(self):
        return str(self.minutes_ones)
    def tick(self):
        self.minutes_ones.increment()
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    clock = Clock12()
    for _ in range(256):
        clock.tick()
    print(clock)