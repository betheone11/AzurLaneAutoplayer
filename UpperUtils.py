import random
import time

import utils
from Contains import Contains
from loguru import logger


# ------------------------------基本操作函数-------------------------------------------------
def yes(index, threshold=0.7):
    # 单击确定键
    conf = 0.9
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    while True:
        if utils.find_image(Contains.src, Contains.yess, conf):
            x, y = utils.find_image(Contains.src, Contains.yess)
            logger.info(utils.tap(x, y, index) + '[点击确定键]')
            time.sleep(random.uniform(0.5, 2))
            break
        else:
            conf -= 0.05
            if conf < threshold:
                raise Exception("couldn't find image")


def cancel(index):
    # 单击红色取消键
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    conf = 0.9
    while True:
        if utils.find_image(Contains.src, Contains.noo, conf):
            x, y = utils.find_image(Contains.src, Contains.noo)
            logger.info(utils.tap(x, y, index) + '[点击取消键]')
            time.sleep(random.uniform(1, 1.5))
            break
        else:
            conf -= 0.05
            if conf < 0.7:
                raise Exception("couldn't find image")


def while_cancel(index):
    # 单击白色取消键
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    conf = 0.9
    while True:
        if utils.find_image(Contains.src, Contains.WhileCancel, conf):
            x, y = utils.find_image(Contains.src, Contains.WhileCancel)
            logger.info(utils.tap(x, y, index) + '[点击取消键]')
            time.sleep(random.uniform(1, 1.5))
            break
        else:
            conf -= 0.05
            if conf < 0.7:
                raise Exception("couldn't find image")


def Continue(index=Contains.index, flag=1):
    # flag=1:点击大获全胜中的点击继续
    # flag=0:获得道具中的点击继续
    temp = None
    conf = 0.9
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    if flag == 1:
        while True:
            if utils.find_image(Contains.src, Contains.TapContinue, confidence=conf):
                logger.info(utils.tap(round(random.uniform(100, 1000), ndigits=3),
                                round(random.choice([random.uniform(100, 282), random.uniform(510, 700)]), ndigits=3),
                                index) + '[随机点击]')
                break
            else:
                conf -= 0.05
                if conf < 0.7:
                    raise Exception("Couldn't find image")
    elif flag == 2:
        while True:
            if utils.find_image(Contains.src, Contains.SmContinue, confidence=conf):
                logger.info(utils.tap(round(random.uniform(100, 1000), ndigits=3),
                                round(random.choice([random.uniform(100, 282), random.uniform(510, 700)]), ndigits=3),
                                index) + '[随机点击]')
                break
            else:
                conf -= 0.05
                if conf < 0.7:
                    raise Exception("Couldn't find image")


# --------------------------------流程控制函数-----------------------------------------------
def init(index, target):
    # 点击想要刷的关卡
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    if utils.find_image(Contains.src, target):
        x, y = utils.find_image(Contains.src, target)
        logger.info(utils.tap(x, y, index) + '[点击进入的关卡]')
    else:
        logger.error("[couldn't find image]")


def start(index):
    # 点击开始前往
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    if utils.find_image(Contains.src, Contains.go):
        x, y = utils.find_image(Contains.src, Contains.go)
        logger.info(utils.tap(x, y, index) + '[点击开始前往]')
    else:
        logger.error("[couldn't find image]")


def clip_select_team(flag=None):
    # 通过索引点击对应的选择舰队
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    team_selector = utils.find_muti_image(src=Contains.src, tar=Contains.Select)
    team_selector = sorted(team_selector, key=lambda a: a['result'][1])
    x1, y1 = team_selector[0]['result']
    x2, y2 = team_selector[1]['result']
    if flag == 1:
        logger.info(utils.tap(x1, y1, 1) + '[点击第一个选择按钮]')
        time.sleep(random.uniform(0.5, 1))
        return f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f'[点击坐标({x1},{y1})][点击选择舰队1]'
    elif flag == 2:
        logger.info(utils.tap(x2, y2, 1) + '[点击第二个选择按钮]')
        time.sleep(random.uniform(0.5, 1))
        return f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]" + f'[点击坐标({x2},{y2})][点击选择舰队2]'


def select_team(flag_1, flag_2, index):
    # 实现作战前选择队伍
    flag = {1: Contains.No1, 2: Contains.No2, 3: Contains.No3, 4: Contains.No4,
            5: Contains.No5, 6: Contains.No6}
    if flag_1 == flag_2:
        raise Exception('输入格式错误')
    elif flag_1 == 1:
        if flag_2 == 2:
            pass
        else:
            clip_select_team(2)
            utils.cf_action(Contains.src, flag[flag_2], index, f'[点击第{flag_2}舰队]')
    elif flag_1 == 2:
        clip_select_team(2)
        utils.cf_action(Contains.src, flag[6], index, f'[点击第6舰队]')
        clip_select_team(1)
        utils.cf_action(Contains.src, flag[flag_1], index, f'[点击第{flag_1}舰队]')
        if flag_2 == 6:
            pass
        else:
            clip_select_team(2)
            utils.cf_action(Contains.src, flag[flag_2], index, f'[点击第{flag_2}舰队]')
    elif flag_2 == 2:
        clip_select_team(1)
        utils.cf_action(Contains.src, flag[flag_1], index, f'[点击第{flag_1}舰队]')
    else:
        clip_select_team(1)
        utils.cf_action(Contains.src, flag[flag_1], index, f'[点击第{flag_1}舰队]')
        clip_select_team(2)
        utils.cf_action(Contains.src, flag[flag_2], index, f'[点击第{flag_2}舰队]')


def gaming_retire(index):
    # 实现作战中退役船
    while True:
        utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
        if utils.find_image(Contains.src, Contains.retire):
            x1, y1 = utils.find_image(Contains.src, Contains.retire)
            logger.info(utils.tap(x1, y1, 1) + '[点击一键退役]')
            time.sleep(random.uniform(0.5, 1.5))
            utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
            if utils.find_image(Contains.src, Contains.over_retire):
                break
            time.sleep(random.uniform(0.5, 1.5))
            yes(index, 0.9)
            time.sleep(random.uniform(0.5, 1.5))
            logger.info(utils.tap(round(random.uniform(100, 1000), ndigits=3),
                            round(random.choice([random.uniform(100, 282), random.uniform(510, 700)]), ndigits=3),
                            1) + '[随机点击]')
            time.sleep(random.uniform(0.5, 1.5))
            yes(index, 0.9)
            time.sleep(random.uniform(0.3, 1))
            yes(index, 0.9)
            time.sleep(random.uniform(0.3, 1))
            logger.info(utils.tap(round(random.uniform(100, 1000), ndigits=3),
                            round(random.choice([random.uniform(100, 282), random.uniform(510, 700)]), ndigits=3),
                            1) + '[随机点击]')
    return logger.info("[退役完成]")


def clear_storehouse(index):
    # 作战中清理仓库
    if utils.find_image(Contains.src, Contains.full_store):
        x, y = utils.find_image(Contains.src, Contains.tidy)
        logger.info(utils.tap(x, y, index) + '[点击整理]')
        time.sleep(random.uniform(1, 1.5))
    try:
        gaming_retire(index)
        time.sleep(random.uniform(1, 1.5))
        cancel(index)
        time.sleep(1)  # 不能删掉，否则会找不到图片或者点击过快无法自律作战（就是卡住了）
        utils.cf_action(Contains.src, Contains.autoplay, index, '[点击自动寻敌]')
    except Exception:
        # 添加自定义异常
        time.sleep(2)
        utils.cf_action(Contains.src, Contains.autoplay, index, '[点击自动寻敌]')
    return logger.info("[清理仓库完成]")


def low_mood(index):
    # 地心情是退出作战
    while_cancel(index)
    utils.cf_action(Contains.src, Contains.Quit, index, '[点击点击撤退]')
    yes(index)


def continue_work(index):
    # 点击再次前往
    if utils.find_image(Contains.src, Contains.working):
        x, y = utils.find_image(Contains.src, Contains.working)
        logger.info(utils.tap(x, y, index) + '[点击再次前往]')


def final_continue(index = Contains.index):
    # 活动或不能自律全部时使用，可以完成结算战斗。
    # 非活动使用时更换图片
    detals = '点击再次前往'
    utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
    if utils.find_image(Contains.src, Contains.SpecAgain, confidence=0.8):
        utils.cf_action(Contains.src, Contains.SpecAgain, index, detals)
    else:
        logger.info(utils.tap(round(random.uniform(100, 1000), ndigits=3),
                        round(random.uniform(640, 720), ndigits=3),
                        index) + '[随机点击]')
        time.sleep(random.uniform(0.8,1.5))
        utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
        while True:
            if utils.find_image(Contains.src, Contains.SpecAgain):
                utils.cf_action(Contains.src, Contains.SpecAgain, index, detals)
                break
            else:
                time.sleep(0.5)
                utils.screen_shot(r'.\icons\AzurLane', title='碧蓝航线')
