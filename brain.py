# coding=utf-8
"""
name whith out '_' = sql func
whith '_' all func
"""

from functions import *
from sql import *

cords_sms = search_BigPurpleButton(None)[0]
cords_call_button = searhc_key_call(None)[0]

text = 'Gj;fkeqcnf j;blfqnt? vs dfv gthtpdjybv/'

if 1 == 1:
    # try:
    while 1 > 0:
        startTime = time.time()
        if not gui.pixelMatchesColor(cords_sms[0], cords_sms[1], (180, 158, 202)): cords_sms = \
            search_BigPurpleButton(None)[0]
        if checkCall() != []:
            hangup(incoming_call())
            time.sleep(0.5)
            for row in checkCall():
                go_to_account(row[0], cords_call_button)
                if not gui.pixelMatchesColor(cords_sms[0], cords_sms[1], (180, 158, 202)): cords_sms = \
                    search_BigPurpleButton(None)[0]
                send_message(text, cords_sms)
                for row in readForEvBack(row[0], '1'):
                    writeToEventsBack(row)
                    clearEvents(row[0])
            print "All calls implode,  " + time.asctime() + ", Elapsed time: {:.3f} sec".format(time.time() - startTime)
        elif checkSms() != []:
            for row in checkSms():
                go_to_account(row[0], cords_call_button)
                if not gui.pixelMatchesColor(cords_sms[0], cords_sms[1], (180, 158, 202)): cords_sms = \
                    search_BigPurpleButton(None)[0]
                send_message(text, cords_sms)
                for row in readForEvBack(row[0], '0'):
                    print str(row) + ''
                    writeToEventsBack(row)
                    clearEvents(row[0])
            print "All sms implode" + time.asctime() + ", Elapsed time: {:.3f} sec".format(time.time() - startTime)
        else:
            print "Why DB clean???  Elapsed time on search: {:.3f} sec".format(time.time() - startTime)
        time.sleep(5)
# except:
#	print "Who all crash?????: {:.3f} sec".format(time.time() - startTime + time.asctime()) + 'Wait 30 sec to return'
#	time.sleep(30)
