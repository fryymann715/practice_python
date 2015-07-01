__author__ = 'Ian'

#import libraries
import webbrowser
import time
import os   #imports filesystem stuff


def take_break(minutes, num_breaks):
    seconds = int(minutes) * 60 #convert minutes to an integer
    break_counter = 0
    print("*************** Started ******************")
    print("******** " + time.ctime() + " ********")
    while break_counter < num_breaks:
        time.sleep(seconds)
        print("testing!")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox/14e38528a5dbdd12")
        break_counter += 1
    print("************** Finished **************")

def rename_files():
    # get file names from this folder
    # the r before the path means raw path
    file_list = os.listdir(r"C:\Users\ideans\Documents\Python_Playground\message_pics")
    print file_list
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\ideans\Documents\Python_Playground\message_pics")
    print(saved_path)
    print(os.getcwd())

    for file_name in file_list:
        #remove numbers and rename file
        os.rename(file_name, file_name.translate(None, "0123456789").lower())
        # take new name and capitalize then rename again
        #os.rename(file_name, file_name.capitalize())
        #print("New name- "+file_name)
    os.chdir(saved_path)
    print(file_list)

rename_files()
