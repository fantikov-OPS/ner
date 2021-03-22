from datetime import timedelta, datetime
import logging
from time import sleep


class Pomodoro:
    def __init__(self, first_name, last_name, focus=1, break_focus=1, cicle=4):
        self.first_name = first_name
        self.last_name = last_name
        self.focus = focus
        self.break_focus = break_focus
        self.cicle = cicle

    def log(self):
        logging.basicConfig(filename="main_log.log", level=logging.INFO)
        logging.info(f'User {self.first_name} {self.last_name} start program from {datetime.now()}')

    def datetime_timer(self):
        print('Work')
        user_time = timedelta(minutes=self.focus)
        one_second = timedelta(seconds=1)
        timer(user_time, one_second)

    def user_break(self):
        print('Break')
        user_time_break = timedelta(minutes=self.break_focus)
        one_second = timedelta(seconds=1)
        timer(user_time_break, one_second)


def timer(user_time, one_second):

    while user_time >= one_second:
        time = user_time - one_second
        user_time = time
        #sleep(1)
        print(f'\r {time}', end='')
        if user_time == timedelta(seconds=0):
            print(' Time out')
    print('Next step')


user = Pomodoro('Alexei', 'Kulik')
for i in range(user.cicle):
    user.log()
    print(user.datetime_timer())
    print(user.user_break())
