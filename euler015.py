__author__ = 'jianxinsun'


def main():
    a=[[0 for x in range(21)] for x in range(21)]
    a[0][0] = 1
    for j in range(20):
        a[0][j+1] = a[0][j]
        a[j+1][0] = a[j][0]
    for i in range(1,21):
        for j in range(1,21):
            a[i][j] = a[i-1][j]+a[i][j-1]
    return a