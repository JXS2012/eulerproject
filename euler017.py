__author__ = 'jianxinsun'


translate_table = ['one','two','three','four','five','six','seven','eight','nine','ten',
                   'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',
                   'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']
def translate_number(n):
    if n>=1000:
        if n%1000>=100:
            return translate_table[n/1000-1]+' '+'thousand '+translate_number(n%1000)
        elif n>1000 and not n%1000==0:
            return translate_table[n/1000-1]+' '+'thousand and '+translate_number(n%1000)
        else:
            return translate_table[n/1000-1]+' '+'thousand'
    if n>100 and not n%100==0:
        return translate_table[n/100-1]+' hundred and '+translate_number(n%100)
    if n>=100 and n%100==0:
        return translate_table[n/100-1]+' hundred'
    if n>=20:
        return translate_table[n/10+17]+' '+translate_number(n%10)
    if n>=10:
        return translate_table[n%10+9]
    if n==0:
        return ''
    return translate_table[n-1]


def count_digits(s):
    return len(s.replace(' ',''))


total_digits = 0
for i in range(1000):
    total_digits+= count_digits(translate_number(i+1))
print total_digits