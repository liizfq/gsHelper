import pyautogui
import time
# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
print("当前屏幕分辨率（%d,%d）"%(screenWidth,screenHeight))
if pyautogui.FAILSAFE==True:
    pyautogui.FAILSAFE=False

# while True:
#     time.sleep(2)
#     currentMouseX, currentMouseY = pyautogui.position()
#     print("(%d,%d)"%(currentMouseX,currentMouseY))

class UnreachClickException(Exception):
    def __init__(self,value):
        self.value=value


def check_point(p):
    return p[0]<screenWidth and p[1]<screenHeight

def click_operation(p):
    if check_point(p):
        pyautogui.moveTo(p)
        pyautogui.click()
    else:
        raise UnreachClickException("点击位置超出了屏幕")

def text_input(text,inteval=0.5,p=None):
    if p !=None:
        click_operation(p)
    pyautogui.typewrite(text,inteval)



if __name__ == '__main__':
    pass