__author__ = 'Ian'

import webbrowser
import time


def to_seconds(hours):
    hours = int(hours) * 60 * 60
    return hours


def take_break(minutes):
    seconds = int(minutes) * 60
    counter = 0
    while counter < 2:
        time.sleep(seconds)
        print("testing!")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox/14e38528a5dbdd12")
        counter += 1




take_break(1)
