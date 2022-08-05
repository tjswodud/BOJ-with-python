h, m = input().split()
h = int(h)
m = int(m)

if (h >= 0 and h <= 23) and (m >= 0 and m <= 59):
    if m < 45:
        if h == 0:
            h = 23
        else:
            h -= 1
        m = 60 - (45 - m)
    else:
        m -= 45

print(h, m)