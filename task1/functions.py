def prod_non_zero_diag(x):
    n = min(len(x), len(x[0]))
    res = 1
    for i in range(n):
        if x[i][i] != 0:
            res *= x[i][i]

    return res 


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    if len(x) != len(y): return False
    for i in range(len(x)):
        if x[i] != y[i]: return False
    return True



def max_after_zero(x):
    maxi = -1e9
    for i in range(1, len(x)):
        if (x[i - 1] == 0 and x[i] > maxi): 
            maxi = x[i]
    if (maxi == -1e9):
        maxi = x[0]
    return maxi



def convert_image(img, coefs):
    a = [[0] * len(img[0]) for y in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            for k in range(3):
                t1 = img[i][j][k]
                t2 = coefs[k]
                a[i][j] += t1 * t2

    return a


def run_length_encoding(x):
    i = 0
    a = []
    b = []
    while (i < len(x)):
        count = 1
        tmp = x[i]
        j = i
        while (j < len(x) - 1):
            if (x[j] == x[j+1]):
                count += 1
                j += 1
            else:
                break
        a.append(tmp)
        b.append(count)
        i = j + 1
    return a, b


def pairwise_distance(x, y):
    m = [[0] * len(y) for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            m[i][j] = ((x[i][0] - y[j][0]) ** 2 + (x[i][1] - y[j][1]) ** 2) ** 0.5
    return m