
#返回next_bigger   还不会
def next_bigger(number):

    # next_bigger(1024) -> 1042
    # next_bigger(1234567980) -> 1234568079
    # next_bigger(9876) -> 9876 9786
    # >>>> show me the code <<<<
    def next_bigger(number):

    nb = str(number)

    try:
        idx_low = [i-1 for i in range(len(nb)-1, 0, -1) if nb[i] > nb[i-1]][0]
        idx_high = idx_low + nb[idx_low:].index([x for x in nb[idx_low:] if x > nb[idx_low]][-1])

        nb_lst = list(nb)
        nb_lst[idx_low], nb_lst[idx_high] = nb_lst[idx_high], nb_lst[idx_low]

        return int(''.join(nb_lst[:idx_low+1] + nb_lst[:idx_low:-1]))

    except IndexError:
        return number
#罗马数字
def num_to_roman(num):

    roman_num = {1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    print(num)
    roman_str = ''

    for key in sorted(roman_num,reverse=True):
        while num>=key:
            roman_str+=roman_num[key]
            num=num-key

    return roman_str

    # >>>> show me the code <<<<