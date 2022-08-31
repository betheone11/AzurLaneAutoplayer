"""
1 后台截图
2 图像识别
3 模拟点击
4 处理异常事件
后期可创造多个实例运用线程池实现一个脚本操控多个模拟器，要对tap等函数的index进行修改
"""
# 后期多任务操作流程运用index随即顺序进行，点击一些无意义点


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
        self.LowMood = 'LowMood.png'
        self.WhileCancel = 'w_no.png'
        self.Quit = 'quit_loop.png'
        self.Select = 'select.png'
        self.No3 = 'No3.png'
        self.No4 = 'No4.png'
        self.No5 = 'No5.png'
        self.No6 = 'No6.png'

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
                time.sleep(random.uniform(0.5, 2))
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
                time.sleep(random.uniform(0.5, 1.5))
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

    def select_team(self,index_1, index_2):
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        team_selecter = utils.find_muti_image(src=self.src, tar=self.Select)
        x1, y1 = team_selecter[0]['result']
        x2, y2 = team_selecter[1]['result']
        # 用字典优化
        utils.tap(x1, y1, 1)
        time.sleep(random.uniform(0.5, 1))
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if index_1 in [1, 2]:
            utils.tap(x1, y1, 1)
            time.sleep(random.uniform(0.5, 1))
        elif index_1 == 3:
            utils.cf_action(self.src, self.No3)
        elif index_1 == 4:
            utils.cf_action(self.src, self.No4)
        elif index_1 == 5:
            utils.cf_action(self.src, self.No5)
        elif index_1 == 6:
            utils.cf_action(self.src, self.No6)
        utils.tap(x2, y2, 1)
        time.sleep(random.uniform(0.5, 1))
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if index_2 in [1, 2, index_1]:
            utils.tap(x2, y2, 1)
            time.sleep(random.uniform(0.5, 1))
        elif index_2 == 3:
            utils.cf_action(self.src, self.No3)
        elif index_2 == 4:
            utils.cf_action(self.src, self.No4)
        elif index_2 == 5:
            utils.cf_action(self.src, self.No5)
        elif index_2 == 6:
            utils.cf_action(self.src, self.No6)

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
                time.sleep(random.uniform(0.5, 1.5))
                utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
                if utils.find_image(self.src, self.over_retire):
                    break
                time.sleep(random.uniform(0.5, 1.5))
                self.yes()
                time.sleep(random.uniform(0.5, 1.5))
                utils.tap(random.uniform(0, 1000), random.uniform(60, 700), 1)
                time.sleep(random.uniform(0.5, 1.5))
                self.yes()
                time.sleep(random.uniform(0.3, 1))
                self.yes()
                time.sleep(random.uniform(0.3, 1))
                utils.tap(random.uniform(0, 1000), random.uniform(60, 700), 1)
        return print('退役完成')

    def clear_storehouse(self):
        # 作战中清理仓库
        if utils.find_image(self.src, self.full_store):
            x, y = utils.find_image(self.src, self.tidy)
            utils.tap(x, y, 1)
            time.sleep(random.uniform(0.5, 1))
        try:
            self.gaming_retire()
            time.sleep(random.uniform(0.5, 1))
            self.cancel()
            utils.cf_action(self.src, self.autoplay)
        except:
            self.cancel()
            time.sleep(random.uniform(1, 1.5))
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
index_1 = int(input('请输入您要出战的第一个舰队：'))
index_2 = int(input('请输入您要出战的第二个舰队：'))
count = 0
sp = Sp()  # 创建实例
# 开始初始化工作：进入要刷的关卡并自动战斗
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.init()
time.sleep(random.uniform(0.8, 1.2))
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.start()
time.sleep(random.uniform(0.8, 1.2))
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
if utils.find_image(sp.src, sp.full_store):  # 判断仓库是否已满
    sp.clear_storehouse()
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    sp.init()
    time.sleep(random.uniform(0.8, 1.2))
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    sp.start()
    time.sleep(random.uniform(0.8, 1.2))
sp.select_team(index_1, index_2)
print('选择舰队完成')
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.start()
# 初始化完成，已进入战斗
for i in range(n):
    count += 1
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    while True:
        sp.continue_work()
        time.sleep(random.uniform(0.5, 1))
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
            time.sleep(random.uniform(4, 8))
    print(f'已完成第{count}轮工作，还剩{n - count}次完成')
print('所有任务已完成')
utils.del_img('{}.png'.format(sp.hwnd))  # 删除运行用的截图，防止使用次数过多后引起脚本占用内存过大
