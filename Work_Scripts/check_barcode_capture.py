'''check_barcode_capture.py
finds if slide has barcode or not
If no barcode wait until barcode
If barcode wait 3 seconds? (change time limit?) and click next


'''
import pyautogui, time

# define images to search for
IMG_ENTER_BARCODE_ID = 'images/enter_barcode_ID.png'
IMG_RIGHT_CLICK = 'images/right_click.png'


def main():
    '''main'''
    print '==> Starting check'
    status = get_status()
    coords = rclick()
    print(coords)
    print(status)
    #if no barcode, wait for barcode
    if status == 'enter barcode':
        print 'no barcode, waiting for input'
    #if barcode, go to next slide
    elif status == 'barcode decoded':
        pyautogui.click(pyautogui.center(coords))
        time.sleep(5)
        pyautogui.moveTo(x=1000, y=700)
    
        #TODO: Fix errors below
'''finds no barcode correctly, but doesn't find when barcode gets entered'''
'''can't find right click button, gives error'''
def get_status():
    '''find if barcode is decoded or needs to be manually entered'''
    status_check = pyautogui.locateOnScreen(IMG_ENTER_BARCODE_ID)
    return status
def rclick():
    '''finds coords of right_click button'''
    coords = pyautogui.locateOnScreen(IMG_RIGHT_CLICK)
    return coords


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            time.sleep(5)