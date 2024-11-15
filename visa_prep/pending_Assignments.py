x,y,z=map(int,input().split())
oneday_time=24*60
total_time=x*y
time_available=z*oneday_time
if total_time<=time_available:
    print('YES')
else:
    print('NO')
