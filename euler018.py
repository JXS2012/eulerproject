__author__ = 'jianxinsun'


def read_triangle(filename):
    f = open(filename,'r')
    text = f.readlines()
    data = []
    for line in text:
        data.append([int(k) for k in line.rstrip('\n').split(' ')])
    return data


def compute_value_function(data):
    value = [[0 for x in range(len(data[y]))] for y in range(len(data))]
    value[0][0] = data[0][0]
    for n in range(len(data)):
        for j in range(len(data[n])):
            if j<n and j>0:
                value[n][j] = data[n][j] + max([value[n-1][j-1],value[n-1][j]])
            else:
                if j==n:
                    value[n][j] = data[n][j] + value[n-1][j-1]
                else:
                    value[n][j] = data[n][j] + value[n-1][j]
    return value

def main():
    data = read_triangle('euler067digits.txt')
    value = compute_value_function(data)
    max_sum = max(value[-1])
    print max_sum


if __name__=="__main__":
    main()