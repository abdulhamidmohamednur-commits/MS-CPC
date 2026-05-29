a, b = map(int, input().split())

shot1 = 0
shot2 = 0

# First shot
for _ in range(a):
    v, c = map(int, input().split())
    shot1 += v * c

# Second shot
for _ in range(b):
    v, c = map(int, input().split())
    shot2 += v * c

if shot1 == shot2:
    print("same")
else:
    print("different")
