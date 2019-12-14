import datetime

from Journal import Journal

journal = Journal('first')

journal.set_new_line('Alex')
journal.set_new_line('Dan')
journal.set_time_start('Alex', datetime.datetime.today() - datetime.timedelta(seconds=36000))
journal.set_time_start('Dan', datetime.datetime.today() - datetime.timedelta(seconds=3600))

journal.fill_line('Alex')
journal.fill_line('Dan')

journal.set_new_line('Alex')
journal.set_new_line('Dan')

journal.set_time_start('Alex', datetime.datetime.today() - datetime.timedelta(seconds=3600))
journal.set_time_start('Dan', datetime.datetime.today() - datetime.timedelta(seconds=7200))

journal.fill_line('Alex')
journal.fill_line('Dan')

journal.set_all_names()
journal.get_total_name_time()
journal.get_total_name_money()


