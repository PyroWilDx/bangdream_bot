import win32gui
import time
import win32com.client


def bluestacks():
    win2find = "BlueStacks"

    while True:
        window = win32gui.FindWindowEx(None, None, None, win2find)
        if not (window == 0):
            win32gui.MoveWindow(window, 0, 0, 1000, 570, True)
            break
        else:
            print("Can\'t find BlueStacks window, please open BlueStacks.")
        time.sleep(1)

    window = win32gui.FindWindowEx(None, None, None, win2find)
    size = win32gui.GetWindowRect(window)

    while size[2] != 1000 or size[3] != 570:
        print("Can\'t setup BlueStacks, please make BlueStacks your Foreground window.")
        window = win32gui.FindWindowEx(None, None, None, win2find)
        win32gui.MoveWindow(window, 0, 0, 1000, 570, True)
        size = win32gui.GetWindowRect(window)
        time.sleep(1)

    window = win32gui.FindWindowEx(None, None, None, win2find)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)
    print("BlueStacks window has been set up, DON\'T move or resize it.")


if __name__ == "__main__":
    bluestacks()
