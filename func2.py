import pyautogui
import time
import urllib2


class Graph(object):
    def __init__(self):
        self.gui = pyautogui
        self.startTime = time.time()
        self.coordinate = self.gui.locateOnScreen('./icons/win32/chat.png', grayscale=True)
        while not self.coordinate:
            self.coordinate = self.gui.locateOnScreen('./icons/win32/chat.png', grayscale=True)
            print "I don't have data"
            time.sleep(1)
#        return self.coordinate


    def send_msg(self,num_tell,msg):
        self.coordinate=self.gui.locateOnScreen('./icons/win32/chat.png', grayscale=True)
        self.gui.click(self.coordinate[0] - 200, self.coordinate[1] - 50)
        time.sleep(2)
        self.gui.click(self.coordinate[0] - 100, self.coordinate[1] + 10)
        time.sleep(2)
        self.gui.typewrite(num_tell)
        self.gui.click(self.coordinate[0], self.coordinate[1] + 100)
        time.sleep(2)
        send_button_coordinate = self.gui.locateOnScreen('./icons/win32/message.png', grayscale=False)
        print send_button_coordinate
        self.gui.click(send_button_coordinate[0] + 100, send_button_coordinate[1] + 32)
        self.gui.typewrite(msg)
        self.gui.press('enter')


    def hangup(self):
        coordinate_call=self.gui.locateOnScreen('./icons/win32/call.png', grayscale=True)
        self.gui.click(coordinate_call[0] +150, coordinate_call[1] + 30)

class get(object):
    @classmethod
    def send_phone(cls,number):
        req = urllib2.urlopen('http://80.73.5.1/viber.php?destination={}'.format(number))
        print req.read()
