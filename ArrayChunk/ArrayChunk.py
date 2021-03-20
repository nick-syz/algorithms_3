# https://skillsmart.ru/algo/15-121-cm/r71p8f1a17.html

def ArrayChunk(M):
    N = len(M) // 2
    i1 = 0
    i2 = len(M)-1
    while True:
        if M[i1] < M[N]:
            i1 += 1
        if M[i2] > M[N]:
            i2 -= 1
        if i1 == i2-1 and M[i1] > M[i2]:
            M[i1], M[i2] = M[i2], M[i1]
            return ArrayChunk(M)
        if i1 == i2 or (i1 == i2-1 and M[i1] < M[i2]):
            return N
        if M[i1] >= M[N] and M[i2] <= M[N]:
            M[i1], M[i2] = M[i2], M[i1]
