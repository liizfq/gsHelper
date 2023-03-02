# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import win32api
import win32gui
import sys
import pyautogui
import win32com.client
import time
import command
from mojo import Event, uninit, ClickEvent, ScanClickEvent
from parm import *
from recognizePic import ocr, match_text
from prtScn import PrtScn
default_width=1920
default_height=1024
from yamltoll import Configuration, PointConf, TextConf, text_conf
from  utils import *






def start_game():
    # conf =event.getConf()
    event_title = "启动游戏客户端"
    target_text = text_conf.get("start_game")
    event=ScanClickEvent("start_game",target_text,None)
    event.process()
    # # 计算游戏窗口的起始桌面坐标
    # text=text_conf.get("start_game")
    # screenshot_pos= get_window_pos(hWnd) if text==uninit else clac_text_pos(hWnd,text)
    # # start_point=(screenshot_pos[0],screenshot_pos[1])
    # print(screenshot_pos)
    # pt = PrtScn("原神", hWnd)
    # # window_pos=get_window_pos(hWnd)
    # img = pt.screenshot(screenshot_pos)
    # # 获取ocr数组
    # ocr_result = ocr(img)
    # # 匹配需要的文字框
    # img_class = match_text(ocr_result, "开始游戏")
    #
    # if img_class==None:
    #     raise Exception("文字识别失败")
    # click_point = img_class.central_point


    # click_point=point_conf.get("start_game")
    #x 1300  y 750
    # if click_point==uninit:

        # c=Configuration("point.yml")
        # conf=c.getConf()
        # conf=None
        # print(conf)

        # 截图

        # conf["x"],conf["y"]=click_point
        # conf["window_pos"]={'left': window_pos[0], 'top': window_pos[1], 'right': window_pos[2], 'bot': window_pos[3]}
        # conf["text_box"]={'left': img_class.resize_left, 'top': img_class.resize_top,
        #                   'right': img_class.resize_right, 'bot':img_class.resize_bot}
    # else:
        # event_title = "根据配置文件的坐标启动游戏客户端"
        # click_point = conf["x"],conf["y"]
        # window_pos=conf["window_pos"]

    # 计算button桌面坐标
    # print("按钮在相对图片的(%d,%d)"%(click_point[0],click_point[1]))
    # img_x_desktop, img_y_desktop = clac_position(click_point,screenshot_pos)
    #
    # print("在桌面(%d,%d)点进行点击" % (img_x_desktop, img_y_desktop))
    # click_event(event_title, (img_x_desktop, img_y_desktop))

def login_game():
    event_title = "进入游戏"
    # text = text_conf.get("enter_game")
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ret = win32api.ShellExecute(1, 'open', '"E:\Genshin Impact\launcher.exe"', '', '', 1)
    import time

    for i in range(0,3):
        hWnd=win32gui.FindWindow(None,"原神")
        if hWnd!=0:
            break
        time.sleep(1)
    else:
        print("程序未启动")
        sys.exit()
    hWnd = win32gui.FindWindow(None, "原神")

    time.sleep(1)
    print("游戏启动器已启动")
    #启动游戏
    sce=ScanClickEvent()
    text="开始游戏"
    sce.load(text, text_conf.get(text), None)
    sce.process()
    time.sleep(10)
    #进入游戏
    text = "点击进人"
    sce.load(text, text_conf.get(text), None,40,3,5)
    sce.process()
    # print(title)
    # print(hWnd)
    # clac_window(hWnd)



    # mid_window_width=window_width/2+left
    # mid_window_height=window_height/2+top
    # print("当前窗口大小(%d,%d)"%(width,height))
    # print("当前窗口中心点：(%d,%d)"%(mid_window_width,mid_window_height))
    # print("当前桌面中心点:(%d,%d)"%(desktop_width/2,desktop_height/2))
    # clac_position()







