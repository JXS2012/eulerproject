__author__ = 'jianxinsun'

('\n'
 'Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.\n'
 'Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.\n'
 '\n'
 'Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.\n'
 '\n'
 'What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefgPeter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.\n'
 'Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.\n'
 '\n'
 'Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.\n'
)

from scipy import misc


def peter(n):
    if n >= 23:
        return peter(45 - n)
    else:
        count = 0
        for k in range((n-9)/4+1):
            j = n-9-4*k
            count += misc.comb(9,k)*misc.comb(9+j-1,j)*((-1)**(k+j*2))
        return count/(4**9)

def colin(n):
    """

    :rtype : float
    """
    if n >= 22:
        return colin(42 - n)
    else:
        count = 0
        for k in range((n-6)/6+1):
            j = n-6-6*k
            count += misc.comb(6,k)*misc.comb(6+j-1,j)*((-1)**(k+j*2))
        return count/(6**6)


def prob():
    probability = 0
    peter_pdf = dict()
    colin_pdf = dict()
    for j in range(6, 37):
        if j >= 9:
            peter_pdf[j] = peter(j)
        else:
            peter_pdf[j] = 0
    for j in range(6, 37):
        colin_pdf[j] = colin(j)
    for i in range(6, 37):
        probability += sum([peter_pdf[j] for j in range(i + 1, 37)]) * colin_pdf[i]
    return probability


if __name__ == "__main__":
    print prob()