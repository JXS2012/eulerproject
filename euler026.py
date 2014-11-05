__author__ = 'jianxinsun'


def get_decimal(nominator, d):
    if nominator in get_decimal.nominator_list:
        return [],nominator
    if nominator == 0:
        return [],nominator
    get_decimal.nominator_list.append(nominator)
    decimal = [nominator/d]
    (decimal_rest,nominator) = get_decimal(nominator%d*10,d)
    decimal += decimal_rest
    return decimal,nominator


def main():
    max_repeating_decimal_len = 0
    max_d = 1
    max_repeating_decimal_list = []
    for i in range(2,1000):
        get_decimal.nominator_list = []
        (decimal, repeating_nominator) = get_decimal(1,i)
        nominator_list = get_decimal.nominator_list
        index = 0
        repeating_decimal_list = decimal[:]
        if repeating_nominator != 0:
            while nominator_list[index] != repeating_nominator:
                repeating_decimal_list.pop(0)
                index += 1
            if len(repeating_decimal_list) > max_repeating_decimal_len:
                max_repeating_decimal_len = len(repeating_decimal_list)
                max_repeating_decimal_list = repeating_decimal_list[:]
                max_d = i
    print max_d
    print max_repeating_decimal_len
    print max_repeating_decimal_list


if __name__=="__main__":
    main()

