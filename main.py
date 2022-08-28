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
import random


class Sp:
    def __init__(self):
        titles = utils.get_all_title()
        hwnds = utils.get_all_handle(titles)
        self.hwnd = hwnds['碧蓝航线']
        self.src = f'{self.hwnd}.png'
        self.target = 'Sp4.png'
        self.go = 'start.png'
        self.working = 'continue_work.png'
        self.full_store = 'full_store.png'
        self.tidy = 'tidy.png'
        self.retire = 'retire.png'
        self.yess = 'yes.png'
        self.noo = 'no.png'
        self.over_retire = 'over_retire.png'
        self.autoplay = 'autoplay.png'

    def init(self):
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(self.src, self.target):
            x, y = utils.find_image(self.src, self.target)
            print(x, y)
            utils.tap(x, y, 1)
        else:
            print("couldn't find image")

    def start(self):
        if utils.find_image(self.src, self.go):
            x, y = utils.find_image(self.src, self.go)
            print(x, y)
            utils.tap(x, y, 1)
        else:
            print("couldn't find image")

    def yes(self):
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        conf = 0.7
        while True:
            if utils.find_image(self.src, self.yess, conf):
                x, y = utils.find_image(self.src, self.yess)
                utils.tap(x, y, 1)
                break
            else:
                conf = conf - 0.1

    def cancel(self):
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        conf = 0.7
        while True:
            if utils.find_image(self.src, self.noo, conf):
                x, y = utils.find_image(self.src, self.noo)
                utils.tap(x, y, 1)
                break
            else:
                conf -= 0.1

    def continue_work(self):
        if utils.find_image(self.src, self.working):
            x, y = utils.find_image(self.src, self.working)
            print(x, y)
            utils.tap(x, y, 1)

    def gaming_retire(self):
        while True:
            utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
            if utils.find_image(self.src, self.retire):
                x1, y1 = utils.find_image(self.src, self.retire)
                utils.tap(x1, y1, 1)
                time.sleep(1)
                utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
                if utils.find_image(self.src, self.over_retire):
                    break
                time.sleep(0.5)
                self.yes()
                time.sleep(0.5)
                utils.tap(500, 500, 1)
                time.sleep(0.5)
                self.yes()
                time.sleep(0.3)
                self.yes()
                time.sleep(0.3)
                utils.tap(500, 500, 1)
        return print('退役完成')

    def clear_storehouse(self):
        if utils.find_image(self.src, self.full_store):
            x, y = utils.find_image(self.src, self.tidy)
            utils.tap(x, y, 1)
            time.sleep(0.5)
        try:
            self.gaming_retire()
            time.sleep(0.5)
            self.cancel()
            utils.cf_action(self.src, self.autoplay)
        except:
            self.cancel()
            time.sleep(1)
            utils.cf_action(self.src, self.autoplay)
        return print('清理仓库完成')


def low_mood():
    pass


ld = r'D:\leidian\LDPlayer4 '
os.chdir(ld)
print('开始运行脚本')
n = int(input('请输入刷多少次'))
sp = Sp()
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.init()
time.sleep(1)
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.start()
time.sleep(1)
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.start()
for i in range(n):
    while True:
        sp.continue_work()
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(sp.src, sp.working):
            break
        elif utils.find_image(sp.src, sp.full_store):
            sp.clear_storehouse()
            continue
        else:
            print("等待本轮完成")
            time.sleep(5)
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    print('已完成一轮工作')
    time.sleep(1)
print('已完成')
utils.del_img('{}.png'.format(sp.hwnd))
