#!/usr/bin/python3
# -*- coding: utf-8 -*

"This module helps to show date and time"
__author__ = "LionNBean"

from datetime import datetime
import calendar

# intro_str = "Current date and time:\n"
# time_now = datetime.now()
# time_str = time_now.strftime("%Y-%m-%d %H:%M:%S")

class Time(datetime):

    @property
    def format_str(self):
        return self._format_str

    @format_str.setter
    def format_str(self, format_value):
        self._format_str = format_value.replace('Y', '%Y')\
            .replace('m', '%m').replace('d', '%d')\
            .replace('H', '%H').replace('M', '%M').replace('S', '%S')

    def show_now(self, value = ''):
        if value == '': print(self.strftime(self._format_str))
        else:  print(self.strftime(value))

    def show_Chinese(self):
        print(self.strftime('\n%Y年%m月%d日 %H时%M分%S秒\n'))

    def show_calendar(self):
        calendar.prmonth(self.year, self.month)


if __name__=="__main__":
    now = Time.now()
    now.show_calendar()
    now.show_Chinese()
    format_str = input('Give me your format: YmdHMS\n')
    now.format_str = format_str
    now.show_now()

    quit = input("\nPress any button to quit.\n")