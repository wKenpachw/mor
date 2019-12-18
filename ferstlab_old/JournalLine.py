import datetime


class JournalLine:
    # Name of the user
    user_name = "someName"
    # start datetime
    d1 = datetime.datetime.today()
    # end datetime
    d2 = datetime.datetime.today()
    # is line full?
    fulled__line = False

    # on init need userName, start and end dates are the datetime of the moment of the work start and the difference = 0
    def __init__(self, name):
        self.d1 = datetime.datetime.today()
        self.d2 = datetime.datetime.today()
        self.fullLine = False
        self.user_name = name

    # setter of start (isn't needed?)
    def set_date_start(self, d1):
        self.d1 = d1

    # setter of end
    def set_date_end(self, d2):
        self.d2 = d2

    def set_full_line_true(self):
        self.fullLine = True

    # to get the total time in minutes, if line isn't full => return zero
    def get_work_time(self):
        if self.fullLine:
            res = self.d2 - self.d1
            return res.total_seconds() // 60
        else:
            return 0

    def get_user_name(self):
        return self.user_name

    def get_is_full(self):
        return self.fullLine
