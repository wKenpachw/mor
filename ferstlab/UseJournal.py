import datetime

from Journal import Journal
import time

journal = Journal('first')

journal.setNewLine('Alex')
journal.setNewLine('Dan')
journal.setTimeStart('Alex', datetime.datetime.today() - datetime.timedelta(seconds=36000))
journal.setTimeStart('Dan', datetime.datetime.today() - datetime.timedelta(seconds=3600))

journal.fillLine('Alex')
journal.fillLine('Dan')

journal.setNewLine('Alex')
journal.setNewLine('Dan')

journal.setTimeStart('Alex', datetime.datetime.today() - datetime.timedelta(seconds=3600))
journal.setTimeStart('Dan', datetime.datetime.today() - datetime.timedelta(seconds=7200))

journal.fillLine('Alex')
journal.fillLine('Dan')

journal.setAllNames()
journal.getTotalNameTime()
journal.getTotalNameMoney()


