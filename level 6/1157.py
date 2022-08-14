count_list = [0 for i in range(26)]
word = list(input())

for character in word:
    if ord(character) >= 97:
        count_list[ord(character) - 97] += 1
    else:
        count_list[ord(character) - 65] += 1

max = 0
alphabet = '?'

for i in range(26):
    if count_list[i] > max:
        max = count_list[i]
        alphabet = chr(i + 65)
    elif count_list[i] == max:
        alphabet = '?'

print(alphabet)