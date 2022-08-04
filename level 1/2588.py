result = 0

num1 = int(input())
num2 = int(input())

remainder = num2 % 10
result += num1 * remainder
print(num1 * remainder)

remainder = (num2 % 100) // 10
result += num1 * remainder * 10
print(num1 * remainder)

remainder = num2 // 100
result += num1 * remainder * 100
print(num1 * remainder)

print(result)