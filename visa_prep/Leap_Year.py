x=int(input().strip())
if x%400 == 0 and x%100==0:
    print('YES')
elif x%4==0 and x%100!=0:
    print('YES')
else:
    print('NO')
