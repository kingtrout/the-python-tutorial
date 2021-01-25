# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was not a valid number!")
#
# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

import sys
#
# try:
#     f = open('sample.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

try:
    raise Exception('Spam', 'Eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)