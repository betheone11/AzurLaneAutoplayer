import utils, time, random
from Contains import Contains


def clip_select_team(index=None):
    # 通过索引点击对应的选择舰队
    utils.screen_shot(r'E:\python project\MyItem\AutoPlayer\icons\AzurLane', title='碧蓝航线')
    team_selector = utils.find_muti_image(src=Contains.src, tar=Contains.Select)
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