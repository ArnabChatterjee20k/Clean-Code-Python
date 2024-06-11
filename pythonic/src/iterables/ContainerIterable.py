from datetime import timedelta,date
class DateRangeContainerIterable:
    """An range that builds its iteration through a generator."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


range1 = DateRangeContainerIterable(date(2022,1,1),date(2022,4,4))
for day in range1:
    print(day)
# we can't call next() here as it is not defined

# no error
print(list(map(str,range1)))