import math

import easyocr
import numpy

ocr_reader=None
import difflib
def ocr(img):
    reader=get_orc_reader()
    result = reader.readtext(img)
    return result

def get_orc_reader():
    global ocr_reader
    if ocr_reader==None:
        ocr_reader=easyocr.Reader(['ch_sim','en']) # 只需要运行一次就可以将模型加载到内存中
    return ocr_reader


class TextImage():
    def __init__(self,left,top,right,bot):
        self.left=left
        self.right=right
        self.top=top
        self.bot=bot
        self.central_point=(int((self.right+self.left)/2),int((self.top+self.bot)/2))
        # # 勾股定理算中心点到四顶角的距离
        # self.hemline=math.sqrt(((self.right-self.left)/2.0)**2+((self.bot-self.top)/2.0)**2)
        # self.x_factor=(self.right-self.left)/2/self.hemline
        # self.y_factor=(self.bot-self.top)/2/self.hemline

        self.offset=((self.right-self.left)/2,(self.bot-self.top)/2)
        #扩大选中的文本框 用于下一次截图识别文字
        self.resize_left=int(self.left-self.offset[0])
        self.resize_right=int(self.right+self.offset[0])
        self.resize_top=int(self.top-self.offset[1])
        self.resize_bot=int(self.bot+self.offset[1])

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

def match_text(result,text):
    for i in result:
        print(i)
        sample_text=i[1]
        if i[1]==text:
            left=i[0][0][0]
            right=i[0][1][0]
            top=i[0][0][1]
            bot=i[0][2][1]
            print("匹配到的图片框：(%d,%d,%d,%d)"%(left,top,right,bot))
            text_image=TextImage(left,top,right,bot)

            return text_image
    else:
        return None
