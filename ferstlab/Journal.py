from datetime import datetime

from JournalLine import JournalLine


class Journal:
    allLines = []
    positionMoney = {'engineer': 100, 'programmer': 150}
    namePosition = {'Alex': 'engineer', 'Dan': 'programmer'}
    allNames = set()
    nowNames = set()
    jName = ""
    nameTime = {}

    nameTime.setdefault('Alex', 0)

    # give name when crate journal
    def __init__(self, name):
        self.jName = name

    # set new line in the journal whith ented name and whit startTime as curent time, if this user allready started print this information
    def setNewLine(self, name):
        if name in self.nowNames:
            print("That user already started")
        else:
            self.allLines.append(JournalLine(name))
            self.nowNames.add(name)
            print("start", name)

    def fillLine(self, name):
        if name in self.nowNames:
            for l in self.allLines:
                if (l.getUserName() == name) and (not l.getIsFull()):
                    l.setDateEnd(datetime.today())
                    l.setFullLineTrue()
                    self.removeNowNames(name)

    def setAllNames(self):
        for l in self.allLines:
            self.allNames.add(l.getUserName())

    def removeNowNames(self, name):
        self.nowNames.remove(name)

    def getTotalNameTime(self):
        for name in self.allNames:
            for l in self.allLines:
                if name == l.getUserName():
                    if not self.nameTime.get(name):
                        self.nameTime.update({name: (l.getWorkTime())})
                    else:
                        self.nameTime.update({name: (self.nameTime.get(name) + l.getWorkTime())})
        print(self.nameTime)

    def getTotalNameMoney(self):
        for name in self.allNames:
            print(name, (self.positionMoney.get(self.namePosition.get(name)) * self.nameTime.get(name))//60)

    def setTimeStart(self, name, dates):
        for l in self.allLines:
            if (not l.getIsFull()) and (l.getUserName() == name):
                l.setDateStart(dates)
