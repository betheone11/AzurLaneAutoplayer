# -*- coding: utf-8 -*-
import ctypes
import inspect
import random
import time

import UpperUtils
import utils
from Contains import Contains

# -----------------------------------------------------------------------------------------
# src = f'{hwnd}.png'
# tag_1 = 'sp3.png'
# tag_2 = 'start.png'
# ld = r'D:\leidian\LDPlayer4 '
# os.chdir(ld)
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane',title='碧蓝航线')
# if utils.find_image(src, tag_1):
#     x, y = utils.find_image(src, tag_1)
#     print(x, y)
#     utils.tap(x, y, 1)
# else:
#     print("could't find image")
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane',title='碧蓝航线')
# if utils.find_image(src, tag_2):
#     x, y = utils.find_image(src, tag_2)
#     print(x, y)
#     utils.tap(x, y)
# else:
#     print("could't find image")
# utils.del_img(r'icons/AzurLane/{}.png'.format(hwnd))
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
# x, y = utils.find_image('{}.png'.format(hwnd), 'tidy.png',confidence=0.7)
# utils.tap(x, y, 1)
# def select_team(src, tag):
#     image = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(src))
#     icon = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(tag))
#     result = ac.find_all_template(image, icon, threshold=0.9)
#     if not result:
#         return None
#     else:
#         return result
# return result
# print(utils.cf_action(b, a))
# detail = select_team(b, a)
# print(detail[0]['result'])
# for i in detail:
#     x, y = i['result']
#     print(x, y)
# print(i)
# detail.append(9)
# if not detail:
#     print(1)
# else:
#     print(0)
# a = 4
# if a in [1, 2]:
#     print(1)
# elif a == 3:
#     print(3)
# elif a == 4:
#     print(4)
# count = 0
# for i in range(6):
#     count += 1
#     while True:
#         a = int(input())
#         if a == 3:
#             print(123131)
#             continue
#         print(1)
#         print('count:', count)
# Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# for i in range(5):
#     print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}]')
#     time.sleep(0.5)
# i = input()
# if i == '1':
#     raise IOError
# while True:
#     print(1)
#     print(2)
#     print(3)
#     print(4)
#     i = int(input())
#     if i != 1:
#         break
# dic = {1: 'index1', 2: 'index2', 3: 'index3', 4: 'index4', 5: 'index5', 6: 'index6'}
# x1 = int(input())
# x2 = int(input())
# if x1 == x2:
#     raise Exception('输入格式错误')
# elif x1 == 1:
#     print('1:p1')
#     if x2 == 2:
#         print('2:p2')
#     else:
#         print('2:', x2)
# elif x1 == 2:
#     print('2:6')
#     print('1:', x1)
#     if x2 == 6:
#         pass
#     else:
#         print('2', x2)
# elif x2 == 2:
#     print('1:', x1)
#     print('2:p2')
# else:
#     print('1:', x1)
#     print('2:', x2)
# hwnd = hwnds['碧蓝航线']
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
# # a = 'quit_loop.png'
# # b = f'{hwnd}.png'
#
#
# utils.tap(600, 600, 1)
# time.sleep(random.uniform(0.5, 1))
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
# if index_1 in [1, 2]:
#     utils.tap(x1, y1, 1)
#     time.sleep(random.uniform(0.5, 1))
# elif index_1 == 3:
#     utils.cf_action(Contains.src, Contains.No3)
# elif index_1 == 4:
#     utils.cf_action(Contains.src, Contains.No4)
# elif index_1 == 5:
#     utils.cf_action(Contains.src, Contains.No5)
# elif index_1 == 6:
#     utils.cf_action(Contains.src, Contains.No6)
# utils.tap(x2, y2, 1)
# time.sleep(random.uniform(0.5, 1))
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
# if index_2 in [1, 2, index_1]:
#     utils.tap(x2, y2, 1)
#     time.sleep(random.uniform(0.5, 1))
# elif index_2 == 3:
#     utils.cf_action(Contains.src, Contains.No3)
# elif index_2 == 4:
#     utils.cf_action(Contains.src, Contains.No4)
# elif index_2 == 5:
#     utils.cf_action(Contains.src, Contains.No5)
# elif index_2 == 6:
#     utils.cf_action(Contains.src, Contains.No6)
# x1 = {'r': (1, 5)}
# x2 = {'r': (1, 4)}
# c = [x1, x2]
# # c = sorted(c, key= lambda a:a['r'][1])
# for i in c:
#     print(i)
# print(round(random.uniform(0, 1000),3))
# UpperUtils.cancel()
# time.sleep(0.5)
# utils.cf_action(Contains.src, Contains.autoplay)
# for i in range(2, 10):
#     print(round(random.choice([random.uniform(100, 282), random.uniform(510, 1000)]), 3))


# from Contains import Contains
# import UpperUtils
# import Contains
# titles = utils.get_all_title()
# hwnds = utils.get_all_handle(titles)
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane',title='碧蓝航线')
# ld = 'D:\leidian\LDPlayer4'
# os.chdir(ld)
# a = os.popen('ldconsole.exe list2', 'r')
# for i in a:
#     print(i)
# utils.tap(434,548,1)
# print(sys.argv)
# utils.screen_shot(r'.\icons\AzurLane',title='碧蓝航线')
# img = ac.imread(r'.\icons\AzurLane\197906.png')
# print(img)


# def find1_image(src, tar, confidence=0.7):
#     # 返回的坐标时相对于应用窗口的坐标
#     image = cv2.imread(r'.\icons\AzurLane\{}'.format(src))
#     icon = cv2.imread(r'.\icons\AzurLane\{}'.format(tar))
#     result = ac.find_template(image, icon, threshold=confidence)
#     if result:
#         x = int(result['result'][0])
#         y = int(result['result'][1])
#         return x, y
#     else:
#         return None


# utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
# image = cv2.imread(r'.\icons\AzurLane\1115724.png')
# icon = cv2.imread(r'.\icons\AzurLane\D3.png')
# result = ac.find_template(image, icon, threshold=0.7)
# print(result)
# src = Contains.src
# tar = Contains.D3
# # print(utils.find_image(src, tar))
# # UpperUtils.init(1, Contains.D3)
# cmd = f'D:&& cd D:\leidian\LDPlayer4 && ld -s 1 input tap 1000 300'
# os.system(cmd)
# ld = r' D:\leidian\LDPlayer4'  # 您的雷电模拟器地址
# ld = ld.strip()
# print(ld[0:2])
# UpperUtils.yes(1, 0.95)
# utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
# print(utils.find_image(Contains.src, Contains.SmContinue))
# utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
# if utils.find_image(Contains.src, Contains.SpecAgain, confidence=0.8):
#     detals = '点击再次前往'
#     utils.cf_action(Contains.src, Contains.SpecAgain,Contains.index,detals)
# else:
#     print(utils.tap(round(random.uniform(100, 1000), 3),
#                     round(random.uniform(640, 720), 3),
#                     Contains.index) + '[随机点击]')
#
'''
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
from AzurLane import Normal_level
import threading

root = tk.Tk()
root.title('MainWindows')
root.geometry('0x0')
root.overrideredirect(True)

azurlane = tk.Toplevel()
azurlane.title('青山碧蓝辅助')
azurlane.geometry('250x300+500+250')
azurlane.resizable(False, False)

azurlane.protocol('WM_DELETE_WINDOW', root.quit)

image = tk.PhotoImage(file=f'icons/AzurLane/bg.png')
tk.Label(azurlane, image=image, bd=0, text='AzurLane', compound='center', font=('幼圆', 20), fg='white').place(
    width=250, height=150)
tk.Label(azurlane, text='请输入次数:').place(width=75, height=25, x=25, y=175)
times = tk.ttk.Combobox(azurlane, values=['1', '3', '5', '10'])
times.place(width=100, height=25, x=100, y=175)
tk.ttk.Button(azurlane, text='开始！', command=lambda: thread_it(Normal_level, args=(times.get()))).place(width=75,
                                                                                                         height=30,
                                                                                                         x=90, y=225)


def thread_it(fc, args=None):
    if args is None:
        args = ()
    else:
        args = args
    t = threading.Thread(target=fc, daemon=True, args=args)
    t.start()


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


root.mainloop()
'''
a = '10'
a = (a,)
print(a)
print(a)