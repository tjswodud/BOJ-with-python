a, b = map(list, input().split())

a.reverse()
b.reverse()

new_a = ''
new_b = ''
for i in range(len(a)):
    new_a += a[i]
    new_b += b[i]

if int(new_a) > int(new_b):
    print(new_a)
else:
    print(new_b)