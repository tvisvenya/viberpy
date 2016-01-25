import pyautogui
import time

gui = pyautogui

# num = '+380935622783'

def send_message(text, coords):
    x, y = coords
    gui.typewrite(text, interval=0)
    gui.click(x, y)


def search_BigPurpleButton(coords):
    while coords == None:
        coords = gui.locateOnScreen('./icons/sendButton.png', grayscale=True)
        if coords == None: print "Warning!!!!   I can't find BigPurpleButton!!!  " + time.asctime()

    coords = gui.center(coords)
    rgb = gui.pixel(coords[0], coords[1])
    return coords,  # rgb


def searhc_key_call(coords=None):
    while coords == None:
        coords = gui.locateOnScreen('./icons/outCall.png', grayscale=True)
        if coords == None: print "Warning!!!!   I can't find BigCallButton!!!  " + time.asctime()
    coords = gui.center(coords)
    rgb = gui.pixel(coords[0], coords[1])
    return coords,  # rgb


def click_call(num, coords):
    x, y = coords
    print coords
    gui.click(x - 440, y - 35)
    gui.click(x - 300, y - 35)
    time.sleep(0.5)
    gui.typewrite(num, interval=0)
    time.sleep(1)
    gui.click(x - 300, y)


def go_to_account(number, coordinates):
    if not gui.pixelMatchesColor(coordinates[0], coordinates[1], (180, 158, 202)): coordinates = searhc_key_call(None)
    click_call(number, coordinates[0])


def incoming_sms():
    return gui.locateOnScreen('./icons/inMsg.png')


def incoming_call(incall=None):

    return gui.locateOnScreen('./icons/inCall.png')


def hangup(coords):
    if coords != None:
        x, y, h, v = coords
        gui.click(x + 200, y + 30)
        return 1
    else:
        return 0
