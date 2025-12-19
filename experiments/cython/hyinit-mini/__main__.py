
from cysignals.signals import sig_check
from time import sleep
import sys


def main():

    print("Hello")
    try:
        # Main program loop
        while True:
            sleep(5)
            sig_check()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


print("Hello" + __name__)
if __name__ == "__main__":
    main()
