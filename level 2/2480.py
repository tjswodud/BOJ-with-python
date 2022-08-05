dice_first, dice_second, dice_third = input().split()
dice_first = int(dice_first)
dice_second = int(dice_second)
dice_third = int(dice_third)

total_prize = 0

if (dice_first == dice_second == dice_third):
    total_prize = 10000 + dice_first * 1000
else:
    if dice_first == dice_second:
        total_prize = 1000 + dice_first * 100
    elif dice_first == dice_third:
        total_prize = 1000 + dice_first * 100
    elif dice_second == dice_third:
        total_prize = 1000 + dice_second * 100
    else:
        if dice_first < dice_second:
            if dice_second > dice_third:
                total_prize = dice_second * 100
            else:
                total_prize = dice_third * 100
        else:
            if dice_first > dice_third:
                total_prize = dice_first * 100
            else:
                total_prize = dice_third * 100

print(total_prize)