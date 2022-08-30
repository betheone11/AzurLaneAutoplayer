"""
1 后台截图
2 图像识别
3 模拟点击
4 处理异常事件
后期可创造多个实例运用线程池实现一个脚本操控多个模拟器，要对tap等函数的index进行修改
"""

# -*- coding: utf-8 -*-
import utils
import os
import time


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
        self.LowMood = 'LowMood.png'
        self.WhileCancel = 'w_no.png'
        self.Quit = 'quit_loop.png'
        self.Select = 'select.png'

    def init(self):
        # 点击想要刷的关卡
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(self.src, self.target):
            x, y = utils.find_image(self.src, self.target)
            print(x, y)
            utils.tap(x, y, 1)
        else:
            print("couldn't find image")

    def start(self):
        # 点击开始前往
        if utils.find_image(self.src, self.go):
            x, y = utils.find_image(self.src, self.go)
            print(x, y)
            utils.tap(x, y, 1)
        else:
            print("couldn't find image")

    def yes(self):
        # 单击确定键
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        conf = 0.7
        while True:
            if utils.find_image(self.src, self.yess, conf):
                x, y = utils.find_image(self.src, self.yess)
                utils.tap(x, y, 1)
                time.sleep(0.8)
                break
            else:
                conf = conf - 0.1

    def cancel(self):
        # 单击红色取消键
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        conf = 0.7
        while True:
            if utils.find_image(self.src, self.noo, conf):
                x, y = utils.find_image(self.src, self.noo)
                utils.tap(x, y, 1)
                time.sleep(0.8)
                break
            else:
                conf -= 0.1

    def while_cancel(self):
        # 单击白色取消键
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        conf = 0.7
        while True:
            if utils.find_image(self.src, self.WhileCancel, conf):
                x, y = utils.find_image(self.src, self.WhileCancel)
                utils.tap(x, y, 1)
                break
            else:
                conf -= 0.1

    def select_team(self):
        team_selecter = utils.find_muti_image(self.src, self.Select)
        # 利用input获得状态码，根据状态码改变编队
        pass

    def continue_work(self):
        # 点击再次前往
        if utils.find_image(self.src, self.working):
            x, y = utils.find_image(self.src, self.working)
            print(x, y)
            utils.tap(x, y, 1)

    def gaming_retire(self):
        # 实现作战中退役船
        while True:
            utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
            if utils.find_image(self.src, self.retire):
                x1, y1 = utils.find_image(self.src, self.retire)
                utils.tap(x1, y1, 1)
                time.sleep(0.8)
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
        # 作战中清理仓库
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

    def low_mood(self):
        # 地心情是退出作战
        self.while_cancel()
        utils.cf_action(self.src, self.Quit)
        self.yes()


ld = r'D:\leidian\LDPlayer4 '
os.chdir(ld)
print('开始运行脚本')
n = int(input('请输入刷多少次'))
count = 0
sp = Sp()  # 创建实例
# 开始初始化工作：进入要刷的关卡并自动战斗
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.init()
time.sleep(1)
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.start()
time.sleep(1)

utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.start()
# 初始化完成，已进入战斗
for i in range(n):
    count += 1
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    while True:
        sp.continue_work()
        time.sleep(0.5)
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(sp.src, sp.working):  # 判断是否结束一轮
            break
        elif utils.find_image(sp.src, sp.full_store):  # 判断仓库是否已满
            sp.clear_storehouse()
            continue
        elif utils.find_image(sp.src, sp.LowMood):  # 判断是否低心情
            sp.low_mood()
            break
        else:
            print("等待本轮完成")
            time.sleep(5)
    print(f'已完成第{count}轮工作，还剩{n - count}次完成')
print('所有任务已完成')
utils.del_img('{}.png'.format(sp.hwnd))  # 删除运行用的截图，防止使用次数过多后引起脚本占用内存过大
