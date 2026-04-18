import sys

# Reading the two integers from standard input
# input() reads one line at a time
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

# Logic based on the comparison of a and b
if a > b:
    print("MAGA!")
elif b > a:
    print("FAKE NEWS!")
else:
    print("WORLD WAR 3!")
