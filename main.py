'''
1 后台截图
2 图像识别
3 模拟点击
4 处理异常事件
'''

# -*- coding: utf-8 -*-
import utils
import os
import time


class Sp3:
    def __init__(self):
        titles = utils.get_all_title()
        hwnds = utils.get_all_handle(titles)
        self.hwnd = hwnds['碧蓝航线']
        self.src = f'{self.hwnd}.png'
        self.tag_1 = 'sp3.png'
        self.tag_2 = 'tag_4.png'
        self.tag_3 = 'continue_work.png'

    def init(self):
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(self.src, self.tag_1):
            x, y = utils.find_image(self.src, self.tag_1)
            print(x, y)
            utils.tap(x, y, 1)
        else:
            print("couldn't find image")

    def start(self):
        if utils.find_image(self.src, self.tag_2):
            x, y = utils.find_image(self.src, self.tag_2)
            print(x, y)
            utils.tap(x, y, 1)
        else:
            print("couldn't find image")

    def continue_work(self):
        if utils.find_image(self.src, self.tag_3):
            x, y = utils.find_image(self.src, self.tag_3)
            print(x, y)
            utils.tap(x, y-50, 1)
        else:
            print("couldn't find image")


def clear_storehouse():
    pass


def low_mood():
    pass


ld = r'D:\leidian\LDPlayer4 '
os.chdir(ld)

print('开始运行脚本')
n = input('请输入刷多少次')
sp3 = Sp3()
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp3.init()
time.sleep(1)
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
time.sleep(1)
sp3.start()
time.sleep(1)
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
time.sleep(1)
sp3.start()
for i in range(3):
    while True:
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(sp3.src, sp3.tag_3):
            break
        else:
            print(1)
            time.sleep(2)
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    time.sleep(0.5)
    sp3.continue_work()
    print('已完成一轮工作')
print('已完成')
utils.del_img(f'.\\icons\\{sp3.hwnd}.png')
