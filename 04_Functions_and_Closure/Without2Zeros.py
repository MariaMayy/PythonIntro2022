def No_2Zero(N, K):
    iCurCount, iCount = 1, 0
    for _ in range(N):
        iCurCount, iCount = (K - 1) * (iCurCount + iCount), iCurCount
    return iCurCount


#print(No_2Zero(33, 33333))