import cv2
import time
import numpy as np
import pyautogui
import setup
from grabscreen import grab_screen
from keyboard import press_and_release, press, release
from colorama import init, Fore

init()

song_choice_var = 2
song_try_counter = 0
is_playing_easy = True
first_time = True
how_much_try = 5


def ask_options():
    global song_choice_var
    global is_playing_easy
    global how_much_try

    try:
        print("Enter 1 to always play the same song")
        print("Enter 2 to play the next song each time")
        print(
            "Enter 3 to try to full-combo every song :\n"
                "   -If the bot doesn't get a full-combo then it plays the song again\n"
                "      -If it doesn't full-combo after X times then it goes to the next song\n"
                "   -If it gets the full combo then it plays the next song that isn't already full-comboed")
        print("Enter 4 to try to full-perfect every song (Same as full-combo but with for full-perfects)")
        song_choice_var = int(input())
        if song_choice_var == 3 or song_choice_var == 4:
            print("Enter 0 if you are playing normal level songs")
            print("Enter 1 if you are playing easy level songs")
            is_playing_easy = bool(int(input()))
            print("How much time do you want the bot to try again if it fails to full-combo/perfect the song ?")
            how_much_try = int(input())
    except ValueError:
        print("You didn't enter 1, 2, 3 or 4 so the bot will play the next song each time (2).")
        song_choice_var = 2

    setup.bluestacks()
    home_to_game()


def play():
    print("Game Start")

    KEY_LIST_FLICK = ['r', 't', 'y']
    KEY_LIST_MAIN = ['f', 'g', 'h']
    KEY_LIST_SECOND = ['v', 'b', 'n']

    NOTE_LOW_RANGE = np.array([169, 74, 255])  # 169, 74, 255
    NOTE_UP_RANGE = np.array([169, 74, 255])
    SKILL_LOW_RANGE = np.array([91, 128, 255])  # 91, 128, 255
    SKILL_UP_RANGE = np.array([91, 128, 255])
    SLIDE_LOW_RANGE = np.array([44, 102, 255])  # 44, 102, 255
    SLIDE_UP_RANGE = np.array([44, 102, 255])
    SLIDE_LINE_LOW_RANGE = np.array([0, 250, 55])  # 0 250 55
    SLIDE_LINE_UP_RANGE = np.array([255, 255, 255])  # 255 255 255
    FLICK_LOW_RANGE = np.array([143, 82, 255])  # 143, 82, 255
    FLICK_UP_RANGE = np.array([146, 90, 255])  # 146, 90, 255

    NOTE_POSITION_LIST = ["Left", "Middle", "Right"]

    FPS_list = []
    last_time = time.time()

    for key in (KEY_LIST_MAIN + KEY_LIST_SECOND + KEY_LIST_FLICK):
        time.sleep(0.1)
        press_and_release(key)
    print("PLAYING")

    last_note_pressed_time = time.time()

    while True:
        screen_main = grab_screen(region=(120, 480, 820, 490))
        screen_main = cv2.cvtColor(screen_main, cv2.COLOR_BGR2HSV)

        screens_list = [screen_main[:, 0:270], screen_main[:, 320:380], screen_main[:, 430:700]]

        masks_list = [cv2.inRange(screens_list[i], NOTE_LOW_RANGE, NOTE_UP_RANGE) for i in range(0, 3)] + \
                     [cv2.inRange(screens_list[i], SKILL_LOW_RANGE, SKILL_UP_RANGE) for i in range(0, 3)] + \
                     [cv2.inRange(screens_list[i], SLIDE_LOW_RANGE, SLIDE_UP_RANGE) for i in range(0, 3)] + \
                     [cv2.inRange(screens_list[i], FLICK_LOW_RANGE, FLICK_UP_RANGE) for i in range(0, 3)]

        findNonZero_list = [cv2.findNonZero(masks_list[i]) for i in range(0, 12)]

        index_nonZero_list = [index for index, value in enumerate(findNonZero_list) if value is not None]

        if len(index_nonZero_list) > 0:
            if all(value <= 2 for value in index_nonZero_list):
                for i in index_nonZero_list:
                    press_and_release(KEY_LIST_MAIN[i])
                    if time.time() - last_note_pressed_time > 0.125:
                        for j in index_nonZero_list:
                            print(Fore.LIGHTCYAN_EX + "NOTE - " + NOTE_POSITION_LIST[j])
                        last_note_pressed_time = time.time()
                # time.sleep(0.025)

            elif all(value >= 9 for value in index_nonZero_list):
                time.sleep(0.045)
                for i in index_nonZero_list:
                    press_and_release(KEY_LIST_FLICK[i - 9])
                    print(Fore.LIGHTMAGENTA_EX + "FLICK")

            else:
                for k in KEY_LIST_MAIN:
                    press(k)
                print(Fore.LIGHTGREEN_EX + "SLIDE" + Fore.WHITE + " / " + Fore.LIGHTYELLOW_EX + "SKILL")

                get_mean = True
                middle_slide = False
                two_slide = False
                x = (120, 820)
                start_time = time.time()
                while True:
                    screen = grab_screen(region=(150, 380, 790, 400))
                    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
                    mask_slide_line = cv2.inRange(screen, SLIDE_LINE_LOW_RANGE, SLIDE_LINE_UP_RANGE)

                    slide_line_nonZero = cv2.findNonZero(mask_slide_line)
                    if slide_line_nonZero is None:
                        if time.time() - start_time > 0.275:
                            time.sleep(0.15)
                        else:
                            time.sleep(0.05)
                        for k in (KEY_LIST_MAIN + KEY_LIST_SECOND):
                            release(k)
                        # time.sleep(0.02)
                        break

                    if get_mean:
                        get_mean = False

                        mean_x = int((sum(slide_line_nonZero) / len(slide_line_nonZero))[0][0])
                        if mean_x <= 280:
                            x = (440, 820)
                        elif mean_x >= 360:
                            x = (120, 500)
                        else:
                            middle_slide = True

                    if not two_slide:
                        if not middle_slide:
                            screen = grab_screen(region=(x[0], 475, x[1], 490))  # 468 500
                        else:
                            img1 = grab_screen(region=(120, 475, 400, 490))
                            img2 = grab_screen(region=(540, 475, 820, 490))
                            screen = np.concatenate((img1, img2), axis=1)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
                        mask_note = cv2.inRange(screen, NOTE_LOW_RANGE, NOTE_UP_RANGE)
                        mask_skill = cv2.inRange(screen, SKILL_LOW_RANGE, SKILL_UP_RANGE)
                        mask_slide = cv2.inRange(screen, SLIDE_LOW_RANGE, SLIDE_UP_RANGE)
                        mask_flick = cv2.inRange(screen, FLICK_LOW_RANGE, FLICK_UP_RANGE)
                        if cv2.findNonZero(mask_note) is not None or cv2.findNonZero(mask_skill) is not None:
                            for k in KEY_LIST_SECOND:
                                press_and_release(k)
                            print(Fore.LIGHTCYAN_EX + "NORMAL" + Fore.WHITE + " / " + Fore.LIGHTYELLOW_EX + "SKILL")
                        if cv2.findNonZero(mask_slide) is not None:
                            for k in KEY_LIST_SECOND:
                                press(k)
                            two_slide = True
                            print(Fore.LIGHTGREEN_EX + "SLIDE")
                        if cv2.findNonZero(mask_flick) is not None:
                            time.sleep(0.045)
                            for k in KEY_LIST_FLICK:
                                press_and_release(k)
                            print(Fore.LIGHTMAGENTA_EX + "FLICK")

                    # show_screen(True) #show screen

        if cv2.countNonZero(cv2.cvtColor(screen_main, cv2.COLOR_RGB2GRAY)) == 0:
            gameEnd_to_home()
            break

        # show_screen(False) #show screen

        FPS_list.append(round(1 / (time.time() - last_time)))
        if len(FPS_list) == 250:
            print("FPS = {}".format(sum(FPS_list) / len(FPS_list)))
            FPS_list = []
        last_time = time.time()


def is_dead():
    pass


def show_screen(showLine):
    NOTE_LOW_RANGE = np.array([169, 74, 255])
    NOTE_UP_RANGE = np.array([169, 74, 255])
    SKILL_LOW_RANGE = np.array([91, 128, 255])
    SKILL_UP_RANGE = np.array([91, 128, 255])
    SLIDE_LOW_RANGE = np.array([44, 102, 255])
    SLIDE_UP_RANGE = np.array([44, 102, 255])
    SLIDE_LINE_LOW_RANGE = np.array([0, 250, 55])
    SLIDE_LINE_UP_RANGE = np.array([255, 255, 255])
    FLICK_LOW_RANGE = np.array([143, 82, 255])
    FLICK_UP_RANGE = np.array([146, 90, 255])

    screen_show = grab_screen(region=(120, 250, 820, 500))
    screen_show = cv2.cvtColor(screen_show, cv2.COLOR_BGR2HSV)

    if not showLine:
        screen_show = cv2.inRange(screen_show, NOTE_LOW_RANGE, NOTE_UP_RANGE) + \
                      cv2.inRange(screen_show, SKILL_LOW_RANGE, SKILL_UP_RANGE) + \
                      cv2.inRange(screen_show, SLIDE_LOW_RANGE, SLIDE_UP_RANGE) + \
                      cv2.inRange(screen_show, SLIDE_LOW_RANGE, SLIDE_UP_RANGE) + \
                      cv2.inRange(screen_show, FLICK_LOW_RANGE, FLICK_UP_RANGE)
    else:
        screen_show = cv2.inRange(screen_show, NOTE_LOW_RANGE, NOTE_UP_RANGE) + \
                      cv2.inRange(screen_show, SKILL_LOW_RANGE, SKILL_UP_RANGE) + \
                      cv2.inRange(screen_show, SLIDE_LOW_RANGE, SLIDE_UP_RANGE) + \
                      cv2.inRange(screen_show, SLIDE_LOW_RANGE, SLIDE_UP_RANGE) + \
                      cv2.inRange(screen_show, FLICK_LOW_RANGE, FLICK_UP_RANGE) + \
                      cv2.inRange(screen_show, SLIDE_LINE_LOW_RANGE, SLIDE_LINE_UP_RANGE)

    cv2.imshow("BOT GLOBAL GAME VIEW", np.array(screen_show))
    cv2.waitKey(1)


def home_to_game():
    global first_time
    global song_try_counter

    while pyautogui.locateOnScreen("live_button.PNG", region=(825, 520, 905, 550), confidence=0.75) is None:
        print("Can\'t find live button, please go to the "
              "home screen of the game (where we see the characters talking)")
        time.sleep(1)
    print("Don\'t move your mouse.")
    time.sleep(1)
    pyautogui.click(860, 500)  # live button
    time.sleep(2)
    pyautogui.click(535, 220)  # free live button
    time.sleep(1)
    pyautogui.click(470, 370)  # no recover button
    while pyautogui.locateOnScreen("confirm_button.PNG", region=(680, 500, 800, 530), confidence=0.75) is None:
        time.sleep(0.5)
    time.sleep(1)

    if song_choice_var == 1:
        time.sleep(1)
        print("Choosing the same song")

    elif song_choice_var == 2:
        if not first_time:
            print("Choosing the next song")
            pyautogui.moveTo(250, 320)
            pyautogui.dragTo(250, 240, duration=1)  # select next song
        else:
            print("Selecting song")
            first_time = False
            time.sleep(1)

    elif song_choice_var == 3:
        time.sleep(1)

        if is_playing_easy:
            x1 = 327
            width = 0
        else:
            x1 = 351
            width = 1

        while pyautogui.locateOnScreen("fullcombostar.png", region=(x1, 267, 27 + width, 28),
                                       confidence=0.75) is not None \
                or pyautogui.locateOnScreen("fullperfectstar.png", region=(x1, 267, 27 + width, 28),
                                            confidence=0.75) is not None:
            print("This song is already full-comboed, selecting next song...")
            pyautogui.moveTo(250, 320)
            pyautogui.dragTo(250, 240, duration=1)  # select next song
            song_try_counter = 0
            time.sleep(1)

        if song_try_counter == how_much_try:
            print("The bot did not succeed to full-combo this song after 5 times, selecting next song...")
            pyautogui.moveTo(250, 320)
            pyautogui.dragTo(250, 240, duration=1)  # select next song
            song_try_counter = 0

        song_try_counter += 1

        if song_try_counter > 1:
            print("Replaying the same song")

    elif song_choice_var == 4:
        time.sleep(1)

        if is_playing_easy:
            x1 = 327
            width = 0
        else:
            x1 = 351
            width = 1

        while pyautogui.locateOnScreen("fullperfectstar.png", region=(x1, 267, 27 + width, 28),
                                       confidence=0.75) is not None:
            print("This song is already full-perfected, selecting next song...")
            pyautogui.moveTo(250, 320)
            pyautogui.dragTo(250, 240, duration=1)  # select next song
            song_try_counter = 0
            time.sleep(1)

        if song_try_counter == how_much_try:
            print("The bot did not succeed to full-perfect this song after 5 times, selecting next song...")
            pyautogui.moveTo(250, 320)
            pyautogui.dragTo(250, 240, duration=1)  # select next song
            song_try_counter = 0

        song_try_counter += 1

        if song_try_counter > 1:
            print("Replaying the same song")

    pyautogui.click(730, 510)  # confirm button
    time.sleep(1)
    pyautogui.click(740, 510)  # start! button
    time.sleep(1)
    pyautogui.click(560, 410)  # ok button
    time.sleep(0.1)
    pyautogui.moveTo(470, 540)  # move to middle
    time.sleep(5)
    while cv2.countNonZero(cv2.cvtColor(grab_screen(region=(904, 64, 906, 66)), cv2.COLOR_RGB2GRAY)) == 0:
        time.sleep(1)
    time.sleep(2)
    while cv2.countNonZero(cv2.cvtColor(grab_screen(region=(120, 465, 820, 500)), cv2.COLOR_RGB2GRAY)) == 0:
        time.sleep(0.5)
    time.sleep(1)
    play()


def gameEnd_to_home():
    print(Fore.WHITE + "Game End")
    KEY_LIST = ['e', 'd', 'c']
    no_live_button = True
    while no_live_button:
        for k in KEY_LIST:
            time.sleep(0.25)
            press_and_release(k)
            screen = grab_screen(region=(820, 70, 850, 95))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(screen, np.array([0, 0, 76]), np.array([0, 0, 79]))
            if cv2.findNonZero(mask) is not None:
                no_live_button = False
                break
    pyautogui.moveTo(570, 100)
    for n in range(0, 4):
        time.sleep(0.25)
        pyautogui.click()
    time.sleep(1)
    home_to_game()


if __name__ == '__main__':
    press_and_release('p', do_press=False, do_release=False)
    ask_options()
