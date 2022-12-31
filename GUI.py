import ctypes
import inspect
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
tk.ttk.Button(azurlane, text='开始！', command=lambda: thread_it(Normal_level, args=times.get())).place(width=75,
                                                                                                         height=30,
                                                                                                         x=90, y=225)


def thread_it(fc, args=None):
    if args is None:
        args = ()
    else:
        args = (args,)
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
