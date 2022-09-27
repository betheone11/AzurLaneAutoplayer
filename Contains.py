import re
import win32gui


def get_all_title():
    # 获取所有的标题并存储在列表中
    windows_list = []
    game_windows_title_list = []
    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windows_list)
    for window in windows_list:
        pattern = re.compile(r'[a-zA-Z\d\u4e00-\u9fa5]')
        title = win32gui.GetWindowText(window)
        if pattern.search(title):
            game_windows_title_list.append(title)
    return game_windows_title_list


def get_all_handle(titles):
    # 返回一个标题：句柄的字典
    hwnds = {}
    for title in titles:
        hwnd = win32gui.FindWindow(0, title)
        hwnds[title] = hwnd
    return hwnds


class Contains:
    # ---------------------------------------------------------------------------------------------
    # 请在此处根据您的环境更改设置
    ld_ad = r'D:\leidian\LDPlayer4'  # 您的雷电模拟器地址
    ld = ld_ad.strip()
    index = 1  # 您的模拟器编号，可以在雷电多开器中查看
    # -------------------------------------------------------------------------------------------
    titles = get_all_title()
    hwnds = get_all_handle(titles)
    hwnd = hwnds['碧蓝航线']
    src = f'{hwnd}.png'
    target = '11_4.png'
    D3 = 'D3.png'
    go = 'start.png'
    working = 'continue_work.png'
    full_store = 'full_store.png'
    tidy = 'tidy.png'
    retire = 'retire.png'
    yess = 'yes.png'
    noo = 'no.png'
    over_retire = 'over_retire.png'
    autoplay = 'autoplay.png'
    LowMood = 'LowMood.png'
    WhileCancel = 'w_no.png'
    Quit = 'quit_loop.png'
    Select = 'select.png'
    No1 = 'No1.png'
    No2 = 'No2.png'
    No3 = 'No3.png'
    No4 = 'No4.png'
    No5 = 'No5.png'
    No6 = 'No6.png'
