import datetime


class JournalLine:
    # Name of the user
    userName = "someName"
    # start datetime
    d1 = datetime.datetime.today()
    # end datetime
    d2 = datetime.datetime.today()
    # is line full?
    fullLine = False

    # on init need userName, start and end dates are the datetime of the moment of the work start and the difference = 0
    def __init__(self, name):
        self.d1 = datetime.datetime.today()
        self.d2 = datetime.datetime.today()
        self.fullLine = False
        self.userName = name

    # setter of start (isn't needed?)
    def setDateStart(self, d1):
        self.d1 = d1

    # setter of end
    def setDateEnd(self, d2):
        self.d2 = d2

    def setFullLineTrue(self):
        self.fullLine = True

    # to get the total time in minutes, if line isn't full => return zero
    def getWorkTime(self):
        if self.fullLine:
            res = self.d2 - self.d1
            return res.total_seconds() // 60
        else:
            return 0

    def getUserName(self):
        return self.userName

    def getIsFull(self):
        return self.fullLine
