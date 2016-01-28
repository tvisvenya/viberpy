text = "Hello World"

from func2 import *
from sql import *
gr = Graph()

#if 1 == 1:
while 1 > 0:
    try:
        startTime = time.time()
        if checkCall() != []:
            gr.hangup()
            for telephone in checkCall():
                gr.send_msg(telephone[0], text)
                for row in readForEvBack(telephone[0], '1'):
                    writeToEventsBack(row)
                    clearEvents(row[0])
            print "All calls implode,  " + time.asctime() + ", Elapsed time: {:.3f} sec".format(time.time() - startTime)
        elif checkSms() != []:
            for telephone in checkSms():
                gr.send_msg(telephone[0], text)
                for row in readForEvBack(telephone[0], '0'):
                    print str(row)
                    writeToEventsBack(row)
                    clearEvents(row[0])
            print "All sms implode" + time.asctime() + ", Elapsed time: {:.3f} sec".format(time.time() - startTime)
        else:
            print "Why DB clean???  Elapsed time on search: {:.3f} sec".format(time.time() - startTime)
        time.sleep(5)
    except:
        print "Who all crash?????: {:.3f} sec".format(time.time() - startTime + time.asctime()) + 'Wait 30 sec to return'
        time.sleep(30)