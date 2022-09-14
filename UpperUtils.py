import utils, time, random
from Contains import Contains


# ------------------------------基本操作函数-------------------------------------------------
def yes():
    # 单击确定键
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    conf = 0.9
    while True:
        if utils.find_image(Contains.src, Contains.yess, conf):
            x, y = utils.find_image(Contains.src, Contains.yess)
            utils.tap(x, y, 1)
            time.sleep(random.uniform(0.5, 2))
            break
        else:
            conf -= 0.05
            if conf < 0.7:
                raise Exception("couldn't find image")


def cancel():
    # 单击红色取消键
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    conf = 0.9
    while True:
        if utils.find_image(Contains.src, Contains.noo, conf):
            x, y = utils.find_image(Contains.src, Contains.noo)
            utils.tap(x, y, 1)
            time.sleep(random.uniform(1, 1.5))
            break
        else:
            conf -= 0.05
            if conf < 0.7:
                raise Exception("couldn't find image")


def while_cancel():
    # 单击白色取消键
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    conf = 0.9
    while True:
        if utils.find_image(Contains.src, Contains.WhileCancel, conf):
            x, y = utils.find_image(Contains.src, Contains.WhileCancel)
            utils.tap(x, y, 1)
            time.sleep(random.uniform(1, 1.5))
            break
        else:
            conf -= 0.05
            if conf < 0.7:
                raise Exception("couldn't find image")


# --------------------------------流程控制函数-----------------------------------------------
def init():
    # 点击想要刷的关卡
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    if utils.find_image(Contains.src, Contains.target):
        x, y = utils.find_image(Contains.src, Contains.target)
        utils.tap(x, y, 1)
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[couldn't find image]")


def start():
    # 点击开始前往
    if utils.find_image(Contains.src, Contains.go):
        x, y = utils.find_image(Contains.src, Contains.go)
        utils.tap(x, y, 1)
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[couldn't find image]")


def clip_select_team(index=None):
    # 通过索引点击对应的选择舰队
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    team_selector = utils.find_muti_image(src=Contains.src, tar=Contains.Select)
    team_selector = sorted(team_selector, key=lambda a: a['result'][1])
    x1, y1 = team_selector[0]['result']
    x2, y2 = team_selector[1]['result']
    if index == 1:
        utils.tap(x1, y1, 1)
        time.sleep(random.uniform(0.5, 1))
        return f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f'[点击坐标({x1},{y1})][点击选择舰队1]'
    elif index == 2:
        utils.tap(x2, y2, 1)
        time.sleep(random.uniform(0.5, 1))
        return f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f'[点击坐标({x2},{y2})][点击选择舰队2]'


def select_team(index_1, index_2):
    # 实现作战前选择队伍
    index = {1: Contains.No1, 2: Contains.No2, 3: Contains.No3, 4: Contains.No4,
             5: Contains.No5, 6: Contains.No6}
    if index_1 == index_2:
        raise Exception('输入格式错误')
    elif index_1 == 1:
        if index_2 == 2:
            pass
        else:
            clip_select_team(2)
            utils.cf_action(Contains.src, index[index_2])
    elif index_1 == 2:
        clip_select_team(2)
        utils.cf_action(Contains.src, index[6])
        clip_select_team(1)
        utils.cf_action(Contains.src, index[index_1])
        if index_2 == 6:
            pass
        else:
            clip_select_team(2)
            utils.cf_action(Contains.src, index[index_2])
    elif index_2 == 2:
        clip_select_team(1)
        utils.cf_action(Contains.src, index[index_1])
    else:
        clip_select_team(1)
        utils.cf_action(Contains.src, index[index_1])
        clip_select_team(2)
        utils.cf_action(Contains.src, index[index_2])


def gaming_retire():
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
            yes()
            time.sleep(random.uniform(0.5, 1.5))
            utils.tap(round(random.uniform(100, 1000), 3), round(random.choice([random.uniform(100, 282), random.uniform(510, 700)]), 3), 1)
            time.sleep(random.uniform(0.5, 1.5))
            yes()
            time.sleep(random.uniform(0.3, 1))
            yes()
            time.sleep(random.uniform(0.3, 1))
            utils.tap(round(random.uniform(100, 1000), 3), round(random.choice([random.uniform(100, 282), random.uniform(510, 700)]), 3), 1)
    return print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[退役完成]")


def clear_storehouse(index):
    # 作战中清理仓库
    if utils.find_image(Contains.src, Contains.full_store):
        x, y = utils.find_image(Contains.src, Contains.tidy)
        utils.tap(x, y, 1)
        time.sleep(random.uniform(0.5, 1))
    try:
        gaming_retire()
        time.sleep(random.uniform(1, 1.5))
        cancel()
        time.sleep(1)  # 不能删掉，否则会找不到图片或者点击过快无法自律作战（就是卡住了）
        if index == 0:
            utils.cf_action(Contains.src, Contains.autoplay)
    except:
        # 添加自定义异常
        time.sleep(2)
        utils.cf_action(Contains.src, Contains.autoplay)
    return print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + "[清理仓库完成]")


def low_mood():
    # 地心情是退出作战
    while_cancel()
    utils.cf_action(Contains.src, Contains.Quit)
    yes()


def continue_work():
    # 点击再次前往
    if utils.find_image(Contains.src, Contains.working):
        x, y = utils.find_image(Contains.src, Contains.working)
        utils.tap(x, y, 1)
