# -*- coding: utf-8 -*-
import utils
import os
import time
import aircv as ac
import win32gui
import random


# import Contains


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


def select_team(src, tag):
    image = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(src))
    icon = ac.imread(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane\{}'.format(tag))
    result = ac.find_all_template(image, icon, threshold=0.9)
    if not result:
        return None
    else:
        return result
    # return result


titles = utils.get_all_title()
hwnds = utils.get_all_handle(titles)
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
dic = {1: 'index1', 2: 'index2', 3: 'index3', 4: 'index4', 5: 'index5', 6: 'index6'}
x1 = int(input())
x2 = int(input())
if x1 == x2:
    raise Exception('输入格式错误')
elif x1 == 1:
    print('1:p1')
    if x2 == 2:
        print('2:p2')
    else:
        print('2:', x2)
elif x1 == 2:
    print('2:6')
    print('1:', x1)
    if x2 == 6:
        pass
    else:
        print('2', x2)
elif x2 == 2:
    print('1:', x1)
    print('2:p2')
else:
    print('1:', x1)
    print('2:', x2)
















# hwnd = hwnds['碧蓝航线']
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
# a = 'quit_loop.png'
# b = f'{hwnd}.png'


# utils.tap(x1, y1, 1)
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

