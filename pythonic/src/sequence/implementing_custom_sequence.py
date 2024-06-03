from collections.abc import Sequence
from datetime import date, timedelta
from typing import Iterator


class DateRange(Sequence):
    def __init__(self, start: date, end: date):
        self._start = start
        self._end = end

    def __len__(self) -> int:
        return (self._end - self._start).days + 1

    def __getitem__(self, item:int|slice):
        if isinstance(item, slice):
            start, stop = item.indices(len(self))
            start_date = self._start + timedelta(days=start)
            end_date = self._start + timedelta(days=stop-1)
            return DateRange(start_date, end_date)
        elif isinstance(item, int):
            if item < 0:
                item += len(self)
            if item < 0 or item >= len(self):
                raise IndexError("Index out of range")
            return self._start + timedelta(days=item)
        else:
            raise TypeError("Invalid argument type")

    def __iter__(self) -> Iterator:
        current = self._start
        end = self._end + timedelta(days=1)
        while current < end:
            yield current
            current += timedelta(days=1)

    def __str__(self) -> str:
        return f"{self._start} to {self._end}"


date_range = DateRange(date(2023, 6, 1), date(2023, 6, 10))
print(len(date_range))
print(date_range[:])

print(list(date_range))