import time

import cv2
import win32gui
import win32ui
import win32con
import numpy as np
import win32com.client
from utils import setAsForegroundWindow,get_genshin_handler

# class Img():
#     def __init__(self,start_point,end_point,img):
#         self.start_point=start_point
#         self.end_point=end_point
#         self.img=img
class PrtScn():
    def __init__(self,name,hWnd=None):
        self.name=name
        self.hWnd=hWnd if hWnd!=None else get_genshin_handler()

    def screenshot(self,window_pos=None):
        if self.name != win32gui.GetWindowText(0):
            setAsForegroundWindow(win32gui.FindWindow(None, self.name))
        # if(text_box==None):
        #     left,top,right,bot = win32gui.GetWindowRect(self.hWnd)
        # else:

        left,top,right,bot=window_pos[0],window_pos[1],window_pos[2],window_pos[3]

        hwndDC= win32gui.GetWindowDC(win32gui.GetDesktopWindow())
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        # rctA = win32gui.GetWindowRect(self.hWnd)
        # w = rctA[2] - rctA[0]
        # h = rctA[3] - rctA[1]
        w= right-left
        h= bot-top
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        result = saveDC.BitBlt((0, 0), (w, h), mfcDC, (left, top), win32con.SRCCOPY)
        signedIntsArray = saveBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype="uint8")
        img.shape = (h, w, 4)
        win32gui.DeleteObject(saveBitMap.GetHandle())
        mfcDC.DeleteDC()
        saveDC.DeleteDC()
        cv2.imshow("a",img)
        cv2.waitKey()
        return img



# import time
# isTrue=True
# for i in range(0,3):
#     hWnd=win32gui.FindWindow(None,"游戏加加")
#     if hWnd!=0:
#         isTrue=False
#         break
#     time.sleep(1)
# else:
#     print("程序未启动")
#     sys.exit()
# time.sleep(1)
# title = win32gui.GetWindowText(hWnd)
# print(title)
# print(hWnd)
# # # 获取句柄窗口的大小信息





# cv2.imshow("s",img)
# cv2.waitKey(0)