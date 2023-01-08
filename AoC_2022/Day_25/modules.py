SNAFU = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
B10 = {0: '0', 1: '1', 2: '2', 3: '=', 4:'-'}

def SNAFU_to_b10(snafu):
    return sum([SNAFU[digit] * 5 ** exp for exp, digit in enumerate(snafu[::-1])])

def b10_to_SNAFU(nb_b10):
    nb_b5 = []
    while nb_b10 > 0 : #change in classic base 5 but nb_b5 is in reverse
        nb_b5.append(nb_b10 % 5)
        nb_b10 = nb_b10 // 5
    remainder = 0
    for i, digit in enumerate(nb_b5):
        nb_b5[i] = B10[(digit + remainder) % len(B10)]
        remainder = 1 if digit in [3, 4] else 0
    return ''.join(nb_b5[::-1]) if remainder == 0 else '1' + ''.join(nb_b5[::-1])