# -*- coding: utf-8 -*-
import utils
import os
import time



titles = utils.get_all_title()
hwnds = utils.get_all_handle(titles)
hwnd = hwnds['碧蓝航线']
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
