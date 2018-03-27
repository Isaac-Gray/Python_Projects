#test
t = int(input())
arr = []
if (t <= 100):
    while (t>0):
        n = int(input()) 
        arr.append("{0:b}".format(n))
        t = t - 1
    for i in arr:
        print(i)

else: print('too large')
