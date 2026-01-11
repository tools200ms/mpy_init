#
# from cysignals.signals import sig_check
# from time import sleep
# import sys
#
# import logging
#
# logging.basicConfig(level=logging.INFO)
# logging.info("Hello")
#
# # def main():
# #
# #     print("Hello",  flush=True)
# #     try:
# #         # Main program loop
# #         while True:
# #             sleep(5)
# #             sig_check()
# #             sys.exit(5)
# #     except Exception as e:
# #         print(f"Error: {e}")
# #         sys.exit(1)
#
#
# print("Hello" + __name__,  flush=True)
# sys.stdout.flush()
#
# sys.exit(56)
#
# # if __name__ == "__main__":
# #     main()
import sys
from time import sleep

print("Hello World from an embedded Cython executable!")
sleep(67)

sys.exit(23)
