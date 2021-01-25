import fibo as fib

# x = int(input("Please enter an integer: "))
x = 0
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Measure some strings:
words = ['Jagger', 'Courtney', 'Mark', 'Hamilton', 'St.Catharine\'s']
#for r in words:
#    print(r, len(r))

#for i in range(20):
#    print(i, end=', ')
#    print('\n')

#for x in range(len(words)):
#    print(x, words[x])

# Search for prime numbers
"""
for n in range(2, 1550):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # print('The loop fell through without finding a factor ')
        print(n, 'is a prime number')
"""

vec = [-4, -2, 0, 2, 4]
# create a new list with the value doubled
vecdouble = [x*2 for x in vec if x >= 0]
print(vecdouble)

fib.fib(500)