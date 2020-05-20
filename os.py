import os
import sys

try:
    print(sys.implementation)
    print(sys.thread_info)
except:
    print('Python3 needed')

print(os.path)

