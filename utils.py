# Add this to __ini__
import time

import pyautogui
import win32com
import win32gui
import command
shell = win32com.client.Dispatch("WScript.Shell")


# And setAsForegroundWindow becomes
def setAsForegroundWindow(hWnd=None):
    handler = hWnd if hWnd != None else get_genshin_handler()
    # 发送ALT键，ALT键使用%号表示
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(handler)
    time.sleep(1)

def clac_position(start_point, position):
    # width, height = getDesktopParm()
    # factor_x = (screenshot_pos[2] - screenshot_pos[0]) / width
    # factor_y = (screenshot_pos[3] - screenshot_pos[1]) / height
    # 计算需要点击的Button相对于桌面分辨率的位置
    point = \
        (start_point[0] * 1 + position[0],
         start_point[1] * 1 + position[1])
    return point


def clac_text_pos(text,hWnd=None):
    handler= hWnd if hWnd!=None else get_genshin_handler()
    window_pos = get_window_pos(handler)
    x_factor = (window_pos[2] - window_pos[0]) / 1920
    y_factor = (window_pos[3] - window_pos[1]) / 1024
    left = int(window_pos[0] + text[0] * x_factor)
    top = int(window_pos[1] + text[1] * y_factor)
    right = int(window_pos[0] + text[2] * x_factor)
    bot = int(window_pos[1] + text[3] * y_factor)
    return (left, top, right, bot)


# # 获取句柄窗口的大小信息
def clac_window(hWnd=None):
    handler = hWnd if hWnd != None else get_genshin_handler()
    left, top, right, bot = win32gui.GetWindowRect(handler)
    print("当前窗口大小(%d,%d,%d,%d)" % (left, top, right, bot))
    # 计算窗口的大小
    global window_width, window_height, window_left, window_top
    window_width = right - left
    window_height = bot - top
    window_left = left
    window_top = top

def get_genshin_handler():
    hWnd = win32gui.FindWindow(None, "原神")
    return hWnd

def get_window_pos(hWnd=None):
    handler= hWnd if hWnd!=None else get_genshin_handler()
    window_pos = win32gui.GetWindowRect(handler)
    return window_pos


def get_start_point(hWnd=None):
    handler = hWnd if hWnd != None else get_genshin_handler()
    w = get_window_pos(handler)
    return (w[0], w[1])


def getDesktopParm():
    width, height = pyautogui.size()
    return (width, height)
