x,y,w,h=map(int,input().split())
dist_x=min(w-x,x)
dist_y=min(h-y,y)
print(min(dist_x,dist_y))