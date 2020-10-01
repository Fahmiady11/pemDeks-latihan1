def N(listData):
    for x in range(len(listData)-1,0,-1):
        for i in range(x):
            if listData[i]>listData[i+1]:
                listData[i],listData[i+1]=listData[i+1],listData[i]
    print("MIN",listData[0])
    print("MIN",listData[len(listData)-1])
x=[100,34,7,2,4,6,77,4,54]
N(x)
