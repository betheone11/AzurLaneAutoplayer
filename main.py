"""
1 后台截图
2 图像识别
3 模拟点击
4 处理异常事件
后期可创造多个实例运用线程池实现一个脚本操控多个模拟器，要对tap等函数的index进行修改
"""
# 后期多任务操作流程运用index随即顺序进行，点击一些无意义点
# 选择出战舰队需要优化
# 将图像识别升级为文字识别
# -*- coding: utf-8 -*-
import utils
import os
import time
import random
import UpperUtils
from Contains import Contains


def continue_work():
    # 点击再次前往
    if utils.find_image(Contains.src, Contains.working):
        x, y = utils.find_image(Contains.src, Contains.working)
        utils.tap(x, y, 1)


class Sp:

    def init(self):
        # 点击想要刷的关卡
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(Contains.src, Contains.target):
            x, y = utils.find_image(Contains.src, Contains.target)
            utils.tap(x, y, 1)
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[couldn't find image]")

    def start(self):
        # 点击开始前往
        if utils.find_image(Contains.src, Contains.go):
            x, y = utils.find_image(Contains.src, Contains.go)
            utils.tap(x, y, 1)
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[couldn't find image]")

    def yes(self):
        # 单击确定键
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        conf = 0.7
        while True:
            if utils.find_image(Contains.src, Contains.yess, conf):
                x, y = utils.find_image(Contains.src, Contains.yess)
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
            if utils.find_image(Contains.src, Contains.noo, conf):
                x, y = utils.find_image(Contains.src, Contains.noo)
                utils.tap(x, y, 1)
                time.sleep(random.uniform(1, 1.5))
                break
            else:
                conf -= 0.1

    def while_cancel(self):
        # 单击白色取消键
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        conf = 0.7
        while True:
            if utils.find_image(Contains.src, Contains.WhileCancel, conf):
                x, y = utils.find_image(Contains.src, Contains.WhileCancel)
                utils.tap(x, y, 1)
                time.sleep(random.uniform(1, 1.5))
                break
            else:
                conf -= 0.1

    def select_team(self, index_1, index_2):
        index = {1: Contains.No1, 2: Contains.No2, 3: Contains.No3, 4: Contains.No4,
                 5: Contains.No5, 6: Contains.No6}
        if index_1 == index_2:
            raise Exception('输入格式错误')
        elif index_1 == 1:
            if index_2 == 2:
                pass
            else:
                UpperUtils.clip_select_team(2)
                utils.cf_action(Contains.src, index[index_2])
        elif index_1 == 2:
            UpperUtils.clip_select_team(2)
            utils.cf_action(Contains.src, index[6])
            UpperUtils.clip_select_team(1)
            utils.cf_action(Contains.src, index[index_1])
            if index_2 == 6:
                pass
            else:
                UpperUtils.clip_select_team(2)
                utils.cf_action(Contains.src, index[index_2])
        elif index_2 == 2:
            UpperUtils.clip_select_team(1)
            utils.cf_action(Contains.src, index[index_1])
        else:
            UpperUtils.clip_select_team(1)
            utils.cf_action(Contains.src, index[index_1])
            UpperUtils.clip_select_team(2)
            utils.cf_action(Contains.src, index[index_2])

    def gaming_retire(self):
        # 实现作战中退役船
        while True:
            utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
            if utils.find_image(Contains.src, Contains.retire):
                x1, y1 = utils.find_image(Contains.src, Contains.retire)
                utils.tap(x1, y1, 1)
                time.sleep(random.uniform(0.5, 1.5))
                utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
                if utils.find_image(Contains.src, Contains.over_retire):
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
        return print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[退役完成]")

    def clear_storehouse(self, index):
        # 作战中清理仓库
        if utils.find_image(Contains.src, Contains.full_store):
            x, y = utils.find_image(Contains.src, Contains.tidy)
            utils.tap(x, y, 1)
            time.sleep(random.uniform(0.5, 1))
        try:
            self.gaming_retire()
            time.sleep(random.uniform(1, 1.5))
            self.cancel()
            if index == 0:
                utils.cf_action(Contains.src, Contains.autoplay)
        except:
            time.sleep(2)
            utils.cf_action(Contains.src, Contains.autoplay)
        return print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[清理仓库完成]")

    def low_mood(self):
        # 地心情是退出作战
        self.while_cancel()
        utils.cf_action(Contains.src, Contains.Quit)
        self.yes()


ld = r'D:\leidian\LDPlayer4'
os.chdir(ld)
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[开始运行脚本]")
n = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[请输入刷多少次]"))
# index_1 = int(input('请输入您要出战的第一个舰队：'))
# index_2 = int(input('请输入您要出战的第二个舰队：'))
count = 0
sp = Sp()  # 创建实例
# 开始初始化工作：进入要刷的关卡并自动战斗
while True:
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    sp.init()
    time.sleep(random.uniform(0.8, 1.2))
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    sp.start()
    time.sleep(random.uniform(0.8, 1.2))
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    if not utils.find_image(Contains.src, Contains.full_store):
        break
    else:
        sp.clear_storehouse(index=1)
# sp.select_team(index_1, index_2)
# print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]"+'[选择舰队完成]')
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
sp.start()
# 初始化完成，已进入战斗
for i in range(n):
    count += 1
    exit_flag = 0
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    while True:
        continue_work()
        time.sleep(random.uniform(0.5, 1))
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(Contains.src, Contains.working):  # 判断是否结束一轮
            break
        elif utils.find_image(Contains.src, Contains.full_store):  # 判断仓库是否已满
            sp.clear_storehouse(index=0)
            continue
        elif utils.find_image(Contains.src, Contains.LowMood):  # 判断是否低心情
            sp.low_mood()  # 图片无法识别准确，改成文字识别并运用正则实现低心情功能
            exit_flag = 1
            break
        else:
            time.sleep(random.uniform(4, 8))
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f"[已完成第{count}轮工作，还剩{n - count}次完成]")
    if exit_flag == 1:  # 低心情时结束任务
        break
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[所有任务已完成]')
utils.del_img('{}.png'.format(Contains.hwnd))  # 删除运行用的截图，防止使用次数过多后引起脚本占用内存过大
