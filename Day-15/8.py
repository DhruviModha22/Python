class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __gt__(self, other):
        return (self.hours * 60 + self.minutes) > (other.hours * 60 + other.minutes)

t1 = Time(2, 30)
t2 = Time(1, 45)
print(t1 > t2)  # Output: True
