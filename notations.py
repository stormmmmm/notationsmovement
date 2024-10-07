def move_to_notation(num, notation):
    if type(num) != int:
        num = int(num)
    res = ""
    if notation <= 10:
        while num != 0:
            res += str(num % notation)
            num //= notation
    else:
        while num != 0:
            res += chr(num % notation + ord('A') - 10)
            num //= notation
    return res[::-1]

def move_from_notation(num, notation):
    res = 0
    if type(num) != str:
        num = str(num)
    for i in range(len(num)):
        alpha = num[i]
        if alpha.isdigit():
            res += int(alpha) * notation ** (len(num) - i - 1)
        else:
            res += (ord(alpha) - ord('A') + 10) * notation ** (len(num) - i - 1)
    return res
