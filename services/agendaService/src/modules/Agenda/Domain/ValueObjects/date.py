from dataclasses import dataclass


@dataclass
class Date:
    day: int
    month: int
    year: int
    
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    def stringToObject(self, date):
        return Date(day=int(date[0:2]), month=int(date[3:5]), year=int(date[6:10]))
    
    def compare(self, date):
        return self.day == date.day and self.month == date.month and self.year == date.year
    
    def inRange(self, start, end):
        return self.day >= start.day and self.month >= start.month and self.year >= start.year and self.day <= end.day and self.month <= end.month and self.year <= end.year