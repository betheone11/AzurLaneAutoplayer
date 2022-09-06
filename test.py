# -*- coding: utf-8 -*-
import utils
import os
import time
import aircv as ac
import win32gui
import random


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
count = 0
for i in range(6):
    count += 1
    while True:
        a = int(input())
        if a == 3:
            print(123131)
            continue
        print(1)
        print('count:', count)
# hwnd = hwnds['碧蓝航线']
# utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
# a = 'quit_loop.png'
# b = f'{hwnd}.png'
