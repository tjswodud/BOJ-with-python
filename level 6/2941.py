word = input()
copy_word = word

while True:
    if 'c=' in copy_word:
        copy_word = copy_word.replace('c=', 'o')
    elif 'c-' in copy_word:
        copy_word = copy_word.replace('c-', 'o')
    elif 'dz=' in copy_word:
        copy_word = copy_word.replace('dz=', 'o')
    elif 'd-' in copy_word:
        copy_word = copy_word.replace('d-', 'o')
    elif 'lj' in copy_word:
        copy_word = copy_word.replace('lj', 'o')
    elif 'nj' in copy_word:
        copy_word = copy_word.replace('nj', 'o')
    elif 's=' in copy_word:
        copy_word = copy_word.replace('s=', 'o')
    elif 'z=' in copy_word:
        copy_word = copy_word.replace('z=', 'o')
    else:
        break

print(len(copy_word))