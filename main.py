import game
from keyboard import press_and_release


def main():
    press_and_release("p", do_press=False, do_release=False)
    game.song_choice()


if __name__ == '__main__':
    main()
