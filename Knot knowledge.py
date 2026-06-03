n = int(input())

need = set(map(int, input().split()))
learned = set(map(int, input().split()))

print((need - learned).pop())
