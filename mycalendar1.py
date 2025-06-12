class MyCalendar:

    def __init__(self):
        self.appointments = []

    def book(self, startTime: int, endTime: int) -> bool:
        for app in self.appointments:
            s, e = app
            if not (endTime <= s or startTime >= e):
                return False

        self.appointments.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
