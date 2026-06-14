#!/usr/bin/python3

import os
import sys

# Get path from environment variable or use default
path = os.environ.get('YINIT_ROOT', '/usr/local/yinit')

if not os.path.exists(path):
    raise FileNotFoundError(f"YInit root path does not exist, YINIT_ROOT: {path}")
if not os.path.isdir(path):
    raise NotADirectoryError(f"Incorrect YInit root path, is should be a directory, YINIT_ROOT: {path}")

sys.path.insert(0, path)

from yinit.main import main

main()
