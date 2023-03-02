import win32gui

from prtScn import PrtScn
from recognizePic import ocr, match_text

hWnd=win32gui.FindWindow(None,"原神")

pt = PrtScn("原神",hWnd)
# c=Configuration("point.yml")
# conf=c.getConf()
# conf=None
# print(conf)
window_pos = win32gui.GetWindowRect(hWnd)
start_point= (window_pos[0],window_pos[2])
# 截图
img = pt.screenshot(window_pos)
# 获取ocr数组
ocr_result = ocr(img)
# 匹配需要的文字框
img_class = match_text(ocr_result, "开始游戏")
click_point = img_class.central_point
window_width=window_pos[2]-window_pos[0]
window_height=window_pos[3]-window_pos[1]

left,top,right,bot=(img_class.resize_left/window_width*1920,
                    img_class.resize_top/window_height*1024,
                    img_class.resize_right / window_width * 1920,
                    img_class.resize_bot / window_height * 1024)
print((left,top,right,bot))
x,y=(click_point[0]/(window_pos[2]-window_pos[0])*1920,click_point[1]/(window_pos[3]-window_pos[1])*1024)
print("(%d,%d)"%(x,y))

