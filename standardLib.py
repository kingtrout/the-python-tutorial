import os
import sys
import argparse
import re
import math
# cwd = os.getcwd()
#
# os_directory = dir(os)
# os_help = help(os)

# print(cwd)

# print(dir(os))

# for x in os_directory:
#     print(x)

# for i in os_help:
#     print(i)

sys.stderr.write('Warning, log file not found. Starting a new one\n')

find_all = re.findall(r'\bf[a-z]*', 'which floor or hand fell fastest')
sub_sub = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

print(find_all)
print(sub_sub)
