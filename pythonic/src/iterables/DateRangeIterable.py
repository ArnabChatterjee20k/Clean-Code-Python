from datetime import timedelta,date
class DateRangeIterable:

    def __init__(self,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date
    
    def __iter__(self):
        return self
        # return DateRangeIterable(self.start_date,self.end_date) 
        ## to encounter the stop iteration protocol we can return a new object with same parameters.
        ## or if we return self we can create new objects everytime
    
    def __next__(self):
        if self._present_day>=self.end_date:
            raise StopIteration
        
        today = self._present_day
        self._present_day+=timedelta(days=1)
        return today

range1 = DateRangeIterable(date(2022,1,1),date(2022,4,4))
for day in range1:
    print(day)
# error StopIteration
print(next(range1))