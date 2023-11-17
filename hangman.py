from engine import *

if __name__ == '__main__':
    while True:
        try:
            play_hangman()
        except KeyboardInterrupt:
            print("\n It's over now. Go home")
            quit()
