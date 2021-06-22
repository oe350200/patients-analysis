import sys

"""Adding documentation locally
Adding documentation remotely """

count = 0

for line in sys.stdin:
    count += 1

print(count, 'lines in standard input')
