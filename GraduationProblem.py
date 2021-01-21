def getNofWays(n):
    absent = [1,2,3]
    total = [2,4,7]
    if(n<=0):
        return 0,0
    if(n<=3):
        return absent[n-1],total[n-1]
    while(n-3>0):
        absent = absent[1:] + [sum(absent)]
        total = total[1:] + [sum(total)]
        n-=1
    return absent[-1],total[-1]

n = int(input())
absent,total=map(str,getNofWays(n))
print('(%s,%s/%s)'%(total,absent,total))