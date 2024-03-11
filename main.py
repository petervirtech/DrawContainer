import pyautogui as p
import time
import datetime

starttime = datetime.datetime.now()
runseconds = 125 * 250
p.FAILSAFE = False
endtime = starttime + datetime.timedelta(0,runseconds) # days, seconds, then other fields.
print(f"will run till {endtime.strftime('%Y-%m-%d %H:%M:%S')}")
for _ in range (250):
    p.press('junja')
    time.sleep(5)
    p.press('junja')
    now = datetime.datetime.now()
 
    print (f"step {_} {now.strftime('%Y-%m-%d %H:%M:%S')} ")
    time.sleep(120)
