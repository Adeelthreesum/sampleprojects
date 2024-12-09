num=[1,2,3,4,5]
farthest=0
jump=0
current=0
for i in range(len(num)-1):
    farthest=max(farthest,i+num[i])
    if i==current:
        jump+=1
        current=farthest
    
    if farthest>=len(num)-1:
        break
    
    
    print(farthest)
    
    
    
print(jump)

