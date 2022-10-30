import time
import easyocr
import pyautogui
from PIL import Image


class MonkeyType:
    """Hack Monkeytype"""
    def __init__(self):
        self.link = 'https://monkeytype.com'
        self.cords = (200, 325, 1550, 415)
        pyautogui.PAUSE = 0.7
        pyautogui.FAILSAFE = True


    def main(self):
        self.open_site()
        self.set_text()


    def open_site(self):
        pyautogui.press('win')
        pyautogui.typewrite('chrome')
        pyautogui.press('enter')
        pyautogui.typewrite(self.link)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('F11')


    def make_screenshot(self):
        time.sleep(0.5)
        self.image = pyautogui.screenshot()
        self.crop_image = self.image.crop(self.cords)
        self.crop_image.save('images/cropped.png')
        self.reader = easyocr.Reader(["en"])
        result = self.reader.readtext('images/cropped.png', detail=0, paragraph=True)
        return result[0]


    def set_text(self):
        text = self.make_screenshot()
        pyautogui.typewrite(text, interval=0.05)
        self.result = pyautogui.confirm('Repeat?', '', ('Yes', 'No'))
        if self.result == 'Yes':
            pyautogui.press('tab')
            pyautogui.press('enter')
            self.set_text()


if __name__ == '__main__':
    solution = MonkeyType()
    solution.main()
