import pywhatkit
import datetime

print(datetime.datetime.now())

numbers = ["+254796871876","+254113349597"]

for i in numbers:
    pywhatkit.sendwhatmsg(i,"Hellow",23,26)