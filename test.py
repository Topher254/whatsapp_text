import pywhatkit
import datetime

time_in_hrs = datetime.datetime.now().hour
time_in_mins = datetime.datetime.now().minute
mina = time_in_mins + 1

pywhatkit.sendwhatmsg("+254113349597","hi",time_in_hrs,mina)