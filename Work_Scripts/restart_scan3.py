'''restart scan if it encounters an error'''
import pyautogui, time

# define images to search for
IMG_START = 'images/start.png'
IMG_STOP = 'images/stop.png'
IMG_BLUE_NO_EYE = 'images/blue_no_eye.png'
IMG_BLUE_W_EYE = 'images/blue_w_eye.png'
IMG_PURPLE_W_EYE = 'images/purple_w_eye.png'
IMG_PURPLE_NO_EYE = 'images/purple_no_eye.png'
IMG_BATCH = 'images/batch.png'
IMG_SNAPSHOTS = 'images/snapshots.png'
IMG_ICON = 'images/icon.png'
IMG_BLUE_BOX = 'images/blue_box.png'
IMG_PURPLE_BOX = 'images/purple_box.png'
IMG_GREEN_BOX = 'images/green_box.png'

currentTime = time.time()
old_len = 0

def main():
    '''main'''
    print '==> Starting check'
    status, coords = get_status()
    if status == 'stopped':
        print 'scanner stopped, hitting start'
        click_in_middle(*coords)

    # coords = list(pyautogui.locateAllOnScreen(IMG_BLUE_NO_EYE))
    # print coords
    # print
    # coords = list(pyautogui.locateAllOnScreen(IMG_BLUE_W_EYE))
    # print coords
    # print
    # coords = list(pyautogui.locateAllOnScreen(IMG_PURPLE_W_EYE))
    # print len(coords)
    # print coords
    # print


def get_status():
    '''find if scanner is running or stopped'''
    coords = pyautogui.locateOnScreen(IMG_START)
    status = 'stopped' if coords else 'running'

    return status, coords
def batch():
    '''move mouse to batch: to allow repeat clicks with get_status()'''
    #TODO: check if coords is not None
    coords = pyautogui.locateOnScreen(IMG_BATCH)
    pyautogui.click(pyautogui.center(coords))


def click_in_middle(pos_x, pos_y, width, height):
    '''click in the middle of a located image'''
    pos_x = pos_x + width / 2
    pos_y = pos_y + height / 2
    pyautogui.click(pos_x, pos_y, button='left')
    time.sleep(5)
    pyautogui.click(pos_x-500, pos_y+500, button='left')
def check_frozen():
	'''check if program is frozen'''
	global currentTime
	global old_len
	'''find if scanner is running or stopped'''
	start_now = pyautogui.locateOnScreen(IMG_STOP)
	if start_now:
		print "start time check"
	else:
		print "not start"
		currentTime = time.time()
	if time.time() - currentTime  < 60:
		coords = list(pyautogui.locateAllOnScreen(IMG_GREEN_BOX))
		#coords += list(pyautogui.locateAllOnScreen(IMG_PURPLE_BOX))
		old_len = len(coords)
		print(old_len)
		print "BLUE_BOX"
		print list(pyautogui.locateAllOnScreen(IMG_GREEN_BOX))
		print "PURPLE_BOX"
		print list(pyautogui.locateAllOnScreen(IMG_PURPLE_BOX))
	elif time.time() - currentTime > 120:
		print 'start check frozen'
		coords1 = list(pyautogui.locateAllOnScreen(IMG_GREEN_BOX))
		#coords1 += list(pyautogui.locateAllOnScreen(IMG_PURPLE_BOX))
		new_len =  len(coords1)
		
		if old_len == new_len:
			print 'Frozen now! send email'
			# reset
			currentTime = time.time()
		else:
                    old_len = new_len
                print(old_len)
                print "BLUE_BOX"
		print list(pyautogui.locateAllOnScreen(IMG_GREEN_BOX))
		print "PURPLE_BOX"
		print list(pyautogui.locateAllOnScreen(IMG_PURPLE_BOX))

def remaximize_window():
	'''check whether window has been minimizem, if true, maximize it'''
	coords = pyautogui.locateOnScreen(IMG_SNAPSHOTS)
	if coords:
		batch()
	else:
		icon_pos = pyautogui.locateOnScreen(IMG_ICON)
		pyautogui.click(pyautogui.center(icon_pos))
		batch()

	
	
	
if __name__ == '__main__':
    while True:
	check_frozen()
        try:
	    main()
			
        except:
            pyautogui.moveTo(100, 100)
        time.sleep(30)
		
