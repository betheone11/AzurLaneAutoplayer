import utils


class Contains:
    titles = utils.get_all_title()
    hwnds = utils.get_all_handle(titles)
    hwnd = hwnds['碧蓝航线']
    src = f'{hwnd}.png'
    target = '11_4.png'
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
