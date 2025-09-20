from math import floor

def tortoise_racing (v1,v2,g):
    if v1 >= v2: return 0
    t = g / (v2-v1)
    return t

time = tortoise_racing(720,850,70)

hour = floor(time)
mins = floor(time * 60)
sec = floor(((time * 60) - mins) * 60)
ans = [hour,mins,sec]

print (ans)
