"""
1 后台截图
2 图像识别
3 模拟点击
4 处理异常事件
后期可创造多个实例运用线程池实现一个脚本操控多个模拟器，要对tap等函数的index进行修改
"""
import os
import random
import time
import UpperUtils
# 后期多任务操作流程运用index随即顺序进行，点击一些无意义点
# 选择出战舰队需要优化
# 将图像识别升级为文字识别
# 学习行为树
# 任务完成后弹窗
# 增加追加次数功能
# -*- coding: utf-8 -*-
import utils
from Contains import Contains

# ---------------------------------------------------------------------------------------------
# 请在此处根据您的环境更改设置
ld = r'D:\leidian\LDPlayer4'  # 您的雷电模拟器地址
index = 1  # 您的模拟器编号，可以在雷电多开器种查看

# -------------------------------------------------------------------------------------------
index_1 = 0
index_2 = 0
target = None
os.chdir(ld)
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[开始运行脚本]")
print('0:刷11-4\n1:刷活动D3')
targets = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[请选择关卡]"))
if targets == 0:
    target = Contains.target
elif targets == 1:
    target = Contains.D3
n = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[请输入刷多少次]"))
select_flag = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[是否进行舰队选择？]'))
if select_flag == 1:
    index_1 = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[请输入您要出战的第一个舰队]'))
    index_2 = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[请输入您要出战的第二个舰队]'))
count = 0
# 开始初始化工作：进入要刷的关卡并自动战斗
while True:
    # 循环体实现作战前清理仓库
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    UpperUtils.init(index, target)
    time.sleep(random.uniform(0.8, 1.2))
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    UpperUtils.start(index)
    time.sleep(random.uniform(0.8, 1.2))
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    if not utils.find_image(Contains.src, Contains.full_store):
        break
    else:
        UpperUtils.clear_storehouse(index=1)
if select_flag == 1:
    UpperUtils.select_team(index_1, index_2, index)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[选择舰队完成]')
utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
UpperUtils.start(index)
# 初始化完成，已进入战斗
for i in range(n):
    count += 1
    exit_flag = 0
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    while True:
        UpperUtils.continue_work(index)
        time.sleep(random.uniform(0.5, 1))
        utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(Contains.src, Contains.working):  # 判断是否结束一轮
            break
        elif utils.find_image(Contains.src, Contains.full_store):  # 判断仓库是否已满
            UpperUtils.clear_storehouse(index=1)
            continue
        elif utils.find_image(Contains.src, Contains.LowMood):  # 判断是否低心情
            UpperUtils.low_mood(index)  # 图片无法识别准确，改成文字识别并运用正则实现低心情功能
            exit_flag = 1
            break
        else:
            time.sleep(random.uniform(4, 8))
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f"[已完成第{count}轮工作，还剩{n - count}次完成]")
    if exit_flag == 1:  # 低心情时结束任务
        break
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[所有任务已完成]')
utils.del_img('{}.png'.format(Contains.hwnd))  # 删除运行用的截图，防止使用次数过多后引起脚本占用内存过大
