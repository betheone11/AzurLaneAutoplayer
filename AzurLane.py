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
def Normal_level():
    n = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[请输入刷多少次]"))
    count = 0
    for i in range(n):
        count += 1
        exit_flag = 0
        utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
        while True:
            UpperUtils.continue_work(Contains.index)
            time.sleep(random.uniform(0.5, 1))
            utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
            if utils.find_image(Contains.src, Contains.working):  # 判断是否结束一轮
                break # 跳出永真循环，计数加一
            elif utils.find_image(Contains.src, Contains.full_store):  # 判断仓库是否已满
                UpperUtils.clear_storehouse(Contains.index)
                continue
            elif utils.find_image(Contains.src, Contains.LowMood):  # 判断是否低心情
                UpperUtils.low_mood(Contains.index)  # 图片无法识别准确，改成文字识别并运用正则实现低心情功能
                exit_flag = 1
                break
            else:
                time.sleep(random.uniform(4, 8))
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f"[已完成第{count}轮工作，还剩{n - count}次完成]")
        if exit_flag == 1:  # 低心情时结束任务
            break
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[所有任务已完成]')
        utils.del_img('{}.png'.format(Contains.hwnd))  # 删除运行用的截图，防止使用次数过多后引起脚本占用内存过大

def fight_royal_maid():
    n = int(input(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[请输入刷多少次]"))
    count = 0
    for i in range(n):
        count += 1
        exit_flag = 0
        utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
        while True:
            utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
            if utils.find_image(Contains.src, Contains.TapContinue):
                UpperUtils.Continue(flag=1)  # 点击继续
                time.sleep(random.uniform(0.8,1.5))
                UpperUtils.Continue(flag=2) # 点击获得道具的继续
                time.sleep(random.uniform(1,1.5))
                utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
                UpperUtils.final_continue() # 结算并点击再次前往
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f"[已完成第{count}轮工作，还剩{n - count}次完成]")
                break # 跳出永真循环，计数加一
            else:
                time.sleep(random.uniform(2, 4))
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + '[所有任务已完成]')
        utils.del_img('{}.png'.format(Contains.hwnd))  # 删除运行用的截图，防止使用次数过多后引起脚本占用内存过大

if __name__ == '__main__':
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[开始运行脚本]")
    #Normal_level()
    fight_royal_maid()
