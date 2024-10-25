import sys
input = sys.stdin.readline

def dot(x:list, y:list):
    result = []
    for i in range(0, 2):
        tmp = []
        for j in range(0, 2):
            tmp.append(x[i][0] * y[0][j] + x[i][1] * y[1][j])
        result.append(tmp)
    return result

if __name__ == '__main__':
    a = [[5, 3],
         [3, 2]]
    b = [[1, 1],
         [1, 0]]
    print(dot(a, b))
