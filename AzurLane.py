# -*- coding: UTF-8 -*-
"""
1 后台截图
2 图像识别
3 模拟点击
4 处理异常事件
后期可创造多个实例运用线程池实现一个脚本操控多个模拟器，要对tap等函数的index进行修改
"""

# todo 优化输入，增加健壮性！ 清理仓库依然存在识别出错问题,开辟一个检测错误的线程，清理仓库完成后关闭
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

index_1 = 0
index_2 = 0
select_flag = 0
target = None
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[开始运行脚本]")
# print('0:刷11-4\n1:刷活动D3')
# targets = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[请选择关卡]"))
# if targets == 0:
#     target = Contains.target
# elif targets == 1:
#     target = Contains.D3
n = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[请输入刷多少次]"))
# select_flag = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[是否进行舰队选择？]'))
# if select_flag == 1:
#     index_1 = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[请输入您要出战的第一个舰队]'))
#     index_2 = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[请输入您要出战的第二个舰队]'))
count = 0
# 开始初始化工作：进入要刷的关卡并自动战斗
# while True:
#     循环体实现作战前1
#     清理仓库
#     UpperUtils.init(1, Contains.D3)
#     time.sleep(random.uniform(0.8, 1.2))
#     UpperUtils.start(Contains.index)
#     time.sleep(random.uniform(0.8, 1.2))
#     utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
#     if not utils.find_image(Contains.src, Contains.full_store):
#         break
#     else:
#         UpperUtils.clear_storehouse(index=1)
# if select_flag == 1:
#     UpperUtils.select_team(index_1, index_2, Contains.index)
#     print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[选择舰队完成]')
# utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
# UpperUtils.start(Contains.index)
# 初始化完成，已进入战斗
for i in range(n):
    count += 1
    exit_flag = 0
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    while True:
        UpperUtils.continue_work(Contains.index)
        time.sleep(random.uniform(0.5, 1))
        utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(Contains.src, Contains.working):  # 判断是否结束一轮
            break
        elif utils.find_image(Contains.src, Contains.full_store):  # 判断仓库是否已满
            UpperUtils.clear_storehouse(Contains.index)
            continue
        elif utils.find_image(Contains.src, Contains.LowMood):  # 判断是否低心情
            UpperUtils.low_mood(Contains.index)  # 图片无法识别准确，改成文字识别并运用正则实现低心情功能
            exit_flag = 1
            break
        else:
            time.sleep(random.uniform(4, 8))
    print(
        f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f"[已完成第{count}轮工作，还剩{n - count}次完成]")
    if exit_flag == 1:  # 低心情时结束任务
        break
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[所有任务已完成]')
utils.del_img('{}.png'.format(Contains.hwnd))  # 删除运行用的截图，防止使用次数过多后引起脚本占用内存过大
