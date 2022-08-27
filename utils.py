import os
import os.path
import aircv as ac
import win32api, win32con, win32gui
import math
from PyQt6.QtWidgets import QApplication
from numpy import array, uint8, ndarray
import sys
import re


# 截图


def get_all_title():
    # 获取所有的标题并存储在列表中
    windows_list = []
    game_windows_title_list = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windows_list)
    for window in windows_list:
        pattern = re.compile(r'[a-zA-Z\d\u4e00-\u9fa5]')
        title = win32gui.GetWindowText(window)
        if pattern.search(title):
            game_windows_title_list.append(title)
    return game_windows_title_list


def get_all_handle(titles):
    # 返回一个标题：句柄的字典
    hwnds = {}
    for title in titles:
        hwnd = win32gui.FindWindow(0, title)
        hwnds[title] = hwnd
    return hwnds


def screen_shot(path, win_class=None, title=None):
    # 实现截图
    hwnd = win32gui.FindWindow(win_class, title)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save(os.path.join(path, f"{hwnd}.png"))


# 屏幕识别匹配对象并返回对应坐标


def find_image(src, tar):
    # 返回的坐标时相对于应用窗口的坐标
    image = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(src))
    icon = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(tar))
    result = ac.find_template(image, icon, 0.7)
    if result:
        x = int(result['result'][0])
        y = int(result['result'][1])
        return x, y
    else:
        return None


# 模拟点击与滑动


def tap(x, y, index):
    cmd = f'ld -s {index} input tap {x} {y}'
    os.popen(cmd)


def swipe(index, x1, y1, x2, y2):
    cmd = f'ld -s {index} input swipe {x1} {y1} {x2} {y2}'
    os.popen(cmd)

def del_img(src):
    os.remove(src)