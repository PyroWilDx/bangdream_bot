import win32gui
import time


def bluestacks():
    win2find = "BlueStacks"
    while True:
        window = win32gui.FindWindowEx(None, None, None, win2find)
        if not (window == 0):
            win32gui.MoveWindow(window, 0, 0, 1000, 570, True)
            print("BlueStacks window has been set up, DON\'T move or resize it")
            break
        else:
            print("Can\'t find BlueStacks window, please open BlueStacks")
        time.sleep(1)
    win32gui.SetForegroundWindow(window)

    # get size while size != 1000 570 dire d'ouvrir bluestacks


if __name__ == "__main__":
    pass
