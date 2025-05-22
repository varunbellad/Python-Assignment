print("Varun Bellad, 1AY24AI096, Sec-O")
# zigzag.py
import time
import sys

indent = 0      # How many spaces to indent
indent_increasing = True

try:
    while True:
        print(' ' * indent + '*')
        time.sleep(0.05)

        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
