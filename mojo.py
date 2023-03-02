import time

import command
from prtScn import PrtScn
from recognizePic import ocr, match_text
from utils import setAsForegroundWindow, get_window_pos, clac_text_pos, clac_position, \
    get_start_point


class YamlFileException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
class Uninitialized():
    def __init__(self):
        pass
    def get(self,*kwargs):
        print("调用了一个未初始化的值")
        return self
    def __eq__(self, other):
        if type(other)==type(self):
            return True
        else:
            return False

class EventProcessException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
#表示未初始化的参数
uninit= Uninitialized()

class EventException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Event():
    def __init__(self):
        self.name=None
        self.isSuccess=None


    def load(self,name):
        self.name = name
        self.isSuccess = None


    def process(self):
        pass

    def run(self):
        try:
            self.process()
        except EventProcessException:
            self.isSuccess=False
        else:
            self.isSuccess=True



class PointUninitException(EventException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)



class ClickEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.point=None


    def load(self,name,point):
        Event.load(self,name)
        self.setPoint(get_start_point(), point)

    def click(self):
        if (self.point == uninit or self.point == None):
            raise PointUninitException("ScanClickEvent:未找到标记点")
        setAsForegroundWindow()
        command.click_operation(self.point)

    def setPoint(self,start_point,point):
        self.point = clac_position(start_point, point) if point !=None else None

    def process(self):
        print("点击事件:%s,坐标(%d,%d)" % (self.name, self.point[0], self.point[1]))
        self.click()

class TextRecognizeException(EventException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class ScanClickEvent(ClickEvent):
    def __init__(self):
        ClickEvent.__init__(self)
        self.target_text=None

    def load(self,name,target_text,point=None,wait=0,times=1,interval=3):
        ClickEvent.load(self,name,point)
        self.target_text = target_text
        self.times=times
        self.interval=interval
        self.wait=wait

    # def reset(self,name,target_text,point=None):
    #     self.name=name
    #     self.target_text=target_text
    #     self.point=point

    def Scan(self):
        screenshot_pos = get_window_pos() if self.target_text == uninit else clac_text_pos(self.target_text)
        print("需要截取的文本框在桌面的(%d,%d,%d,%d)"%(screenshot_pos))
        # start_point=(screenshot_pos[0],screenshot_pos[1])
        # print(screenshot_pos)
        pt = PrtScn("原神")
        # window_pos=get_window_pos(hWnd)
        img_class = None
        if(self.wait!=0):
            time.sleep(self.wait)
        for i in range(0,self.times):
            img = pt.screenshot(screenshot_pos)
            # 获取ocr数组
            ocr_result = ocr(img)
            # 匹配需要的文字框
            img_class = match_text(ocr_result, self.name)
            if img_class != None:
                break
            else:
                time.sleep(self.interval)
        if img_class == None:
            raise TextRecognizeException("文字识别失败")
        start_pos=(screenshot_pos[0],screenshot_pos[1])
        # resize_point=clac_position(start_pos,img_class.central_point)
        ClickEvent.setPoint(self,start_pos,img_class.central_point)

    def process(self):
        self.Scan()
        ClickEvent.process(self)

class Job():
    def __init__(self):
        self.events=[]


    def process(self):
        for event in self.events:
            if(event.isSuccess==None):
                event.run()
            elif event.isSuccess==False:
                event.run()



