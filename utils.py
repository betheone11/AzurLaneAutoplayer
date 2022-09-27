import os
import os.path
import random
import sys
import time
import aircv as ac
import cv2
import win32gui
from PyQt6.QtWidgets import QApplication
from Contains import Contains


# 截图


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
    image = cv2.imread(r'.\icons\AzurLane\{}'.format(src))
    icon = cv2.imread(r'.\icons\AzurLane\{}'.format(tar))
    result = ac.find_template(image, icon, threshold=confidence)
    if result:
        x = int(result['result'][0])
        y = int(result['result'][1])
        return x, y
    else:
        return None


def find_muti_image(src, tar, confidence=0.9):
    # 同个图片内查询多个单位
    image = cv2.imread(r'.\icons\AzurLane\{}'.format(src))
    icon = cv2.imread(r'.\icons\AzurLane\{}'.format(tar))
    result = ac.find_all_template(image, icon, threshold=confidence)
    if not result:
        return None
    else:
        return result


def cf_action(src, tag, index, detals=''):
    # 找图，点图等反馈的集大成者！ 逢魔函数！
    screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    conf = 0.9
    while True:
        if find_image(src, tag, conf):
            x, y = find_image(src, tag)
            print(tap(x, y, index) + detals)
            break
        else:
            if conf < 0.7:
                raise IOError
            else:
                conf -= 0.05
    time.sleep(random.uniform(0.5, 1.5))


# 模拟点击与滑动


def tap(x, y, index):
    cmd = f'{Contains.ld[:2]}&& cd {Contains.ld} &&' \
          f'ld -s {index} input tap {x + random.randint(-5, 5)} {y - 34 + random.randint(-5, 5)}'
    os.popen(cmd)
    return f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f"[点击坐标({x},{y})]"


def swipe(index, x1, y1, x2, y2):
    cmd = f'{Contains.ld[:2]}&& cd {Contains.ld} &&' \
          f'ld -s {index} input swipe {x1 + random.randint(-5, 5)} \
{y1 - 34 + random.randint(-5, 5)} {x2 + random.randint(-5, 5)} {y2 - 34 + random.randint(-5, 5)} '
    os.popen(cmd)


def del_img(src):
    os.remove(r'.\icons\AzurLane\{}'.format(src))
