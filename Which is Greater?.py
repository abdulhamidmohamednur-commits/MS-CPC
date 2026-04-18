import sys

def solve():
    # Read the single line of input and split it into two variables
    try:
        line = sys.stdin.read().split()
        if not line:
            return
        
        a = int(line[0])
        b = int(line[1])

        # Output 1 if a > b, else 0
        if a > b:
            print(1)
        else:
            print(0)
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
