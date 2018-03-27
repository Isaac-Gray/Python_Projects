print('hello world')
name = input("please enter the name of whom I am greeting")
greeting = "Hello! "
print( greeting + name)
for i in range (0, 4):
    print(i)
print("starting test")

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
