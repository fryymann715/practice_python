__author__ = 'Ian'

import webbrowser
import time


def take_break(minutes, num_breaks):
    seconds = int(minutes) * 60
    break_counter = 0
    print("*************** Started ******************")
    print("******** " + time.ctime() + " ********")
    while break_counter < num_breaks:
        time.sleep(seconds)
        print("testing!")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox/14e38528a5dbdd12")
        break_counter += 1
    print("************** Finished **************")



take_break(1, 3)
