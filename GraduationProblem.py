#Using Dynammic Programming
def getNofWays(n):
    #n=1==> 1 | 0 (absent:1 || total:2) (last day not attend - 1)
    #we add a day before and calculate nof ways for every iteration
    #n=2==> 11 | 01 | 10 | 00 (total:4 || absent:2 (10|00))
    #n=3==> 111 | 011 | 101 | 001 | 110 | 010 | 100 (total:7 || absent:3) (000 as three consecutive days not valid)
    """n=4==> from the first 4 combinations of n=3, 
    it is observed that it is same as n=2 with last day removed, so by adding a day result will become n=3(7) combinations
    | next 2 combinations, it is observed that it is same as n=1 with last 2 days removed, 
    so by adding a day result will become n=2(4) combinations
    | next 1 combination, there can be 2 ways for a day to be inserted, so by adding a day result will become n=1(2) combinations
    So, n=4 will be (n=3)+(n=2)+(n=1)
    and so on..
    """
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