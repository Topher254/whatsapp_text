import pywhatkit
import datetime

time_in_hrs = datetime.datetime.now().hour
time_in_mins = datetime.datetime.now().minute
mins = time_in_mins + 1

messager = "Hi there, We offer quality assignment help"

print(datetime.datetime.now())

numbers = ["+254796871876","+254113349597"]

for i in numbers:
    pywhatkit.sendwhatmsg(i,messager,time_in_hrs,mins)

    mins = mins+1
    