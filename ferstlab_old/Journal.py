from datetime import datetime

from JournalLine import JournalLine


class Journal:
    all_lines = []
    position_money = {'engineer': 100, 'programmer': 150}
    name_position = {'Alex': 'engineer', 'Dan': 'programmer'}
    all_names = set()
    now_names = set()
    journal_name = ""
    name_time = {}

    # name_time.setdefault('Alex', 0)

    # give name when crate journal
    def __init__(self, name):
        self.journal_name = name

    # set new line in the journal with entered name and whit startTime as current time,
    # if this user already started print this information
    def set_new_line(self, name):
        if name in self.now_names:
            print("That user already started")
        else:
            self.all_lines.append(JournalLine(name))
            self.now_names.add(name)
            print("start", name)

    def fill_line(self, name):
        if name in self.now_names:
            for l in self.all_lines:
                if (l.get_user_name() == name) and (not l.get_is_full()):
                    l.set_date_end(datetime.today())
                    l.set_full_line_true()
                    self.remove_now_names(name)

    def set_all_names(self):
        for l in self.all_lines:
            self.all_names.add(l.get_user_name())

    def remove_now_names(self, name):
        self.now_names.remove(name)

    def get_total_name_time(self):
        for name in self.all_names:
            for l in self.all_lines:
                if name == l.get_user_name():
                    if not self.name_time.get(name):
                        self.name_time.update({name: (l.get_work_time())})
                    else:
                        self.name_time.update({name: (self.name_time.get(name) + l.get_work_time())})
        print(self.name_time)

    def get_total_name_money(self):
        for name in self.all_names:
            print(name, (self.position_money.get(self.name_position.get(name)) * self.name_time.get(name)) // 60)

    def set_time_start(self, name, dates):
        for l in self.all_lines:
            if (not l.get_is_full()) and (l.get_user_name() == name):
                l.set_date_start(dates)
