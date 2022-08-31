import os
import os.path
import random
import re
import sys
import time
import aircv as ac
import win32gui
from PyQt6.QtWidgets import QApplication


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


def find_image(src, tar, confidence=0.7):
    # 返回的坐标时相对于应用窗口的坐标
    image = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(src))
    icon = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(tar))
    result = ac.find_template(image, icon, confidence)
    if result:
        x = int(result['result'][0]) + random.randint(-5, 5)
        y = int(result['result'][1]) + random.randint(-5, 5)
        return x, y
    else:
        return None


def find_muti_image(src, tar, confidence=0.9):
    # 同个图片内查询多个单位
    image = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(src))
    icon = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(tar))
    result = ac.find_all_template(image, icon, threshold=confidence)
    if not result:
        return None
    else:
        return result


def cf_action(src, tag):
    # 找图，点图等反馈的集大成者！ 逢魔函数！
    screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    conf = 0.9
    while True:
        if find_image(src, tag, conf):
            x, y = find_image(src, tag)
            tap(x, y, 1)
            break
        else:
            conf -= 0.05
    time.sleep(random.uniform(0.5, 1.5))


# 模拟点击与滑动


def tap(x, y, index):
    cmd = f'ld -s {index} input tap {x + random.randint(-5, 5)} {y - 42 + random.randint(-5, 5)}'
    os.popen(cmd)


def swipe(index, x1, y1, x2, y2):
    cmd = f'ld -s {index} input swipe {x1 + random.randint(-5, 5)} \
{y1 - 42 + random.randint(-5, 5)} {x2 +random.randint(-5, 5)} {y2 - 42 + random.randint(-5, 5)} '
    os.popen(cmd)


def del_img(src):
    os.remove(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(src))
