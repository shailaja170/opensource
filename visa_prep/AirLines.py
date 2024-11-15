x,y=map(int,input().split())
planes_required=(y+99)//100
planes_need=max(0,planes_required-x)
print(planes_need)
