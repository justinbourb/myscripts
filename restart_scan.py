'''restart scan if it encounters an error'''
import pyautogui, time

# define images to search for
IMG_START = 'images/start.png'
IMG_STOP = 'images/stop.png'
IMG_BLUE_NO_EYE = 'images/blue_no_eye.png'
IMG_BLUE_W_EYE = 'images/blue_w_eye.png'
IMG_PURPLE_W_EYE = 'images/purple_w_eye.png'


def main():
    '''main'''
    print '==> Starting check'
    status, coords = get_status()
    if status == 'stopped':
        print 'scanner stopped, hitting start'
        click_in_middle(*coords)

    coords = list(pyautogui.locateAllOnScreen(IMG_BLUE_NO_EYE))
    print coords
    print
    coords = list(pyautogui.locateAllOnScreen(IMG_BLUE_W_EYE))
    print coords
    print
    coords = list(pyautogui.locateAllOnScreen(IMG_PURPLE_W_EYE))
    print len(coords)
    print coords
    print


def get_status():
    '''find if scanner is running or stopped'''
    coords = pyautogui.locateOnScreen(IMG_START)
    status = 'stopped' if coords else 'running'

    return status, coords


def click_in_middle(pos_x, pos_y, width, height):
    '''click in the middle of a located image'''
    pos_x = pos_x + width / 2
    pos_y = pos_y + height / 2
    pyautogui.click(pos_x, pos_y, button='left')
    time.sleep(1)
    pyautogui.moveTo(10, 10)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(30)
