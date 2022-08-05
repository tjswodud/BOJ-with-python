a, b = input().split()
a = int(a)
b = int(b)
c = int(input())

result_hour = a
result_minute = b

if (a >= 0 and a <= 23) and (b >= 0 and b <= 59) and (c >= 0 and c <= 1000):
    remainder = (b + c) % 60
    quotient = (b + c) // 60

    if quotient > 0:
        if result_hour + quotient > 23:
            result_hour = (result_hour + quotient) - 24
        else:
            result_hour = result_hour + quotient
        
        result_minute = remainder
    else:
        result_minute = remainder

print(result_hour, result_minute)