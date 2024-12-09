class Twosum:
    def Sum(self):
        input=[4,2,3]
        target=6
        hashmap={}
        sum=0
        for i in range(len(input)):
            
            
            #print(i,input[i])
            sum=target-input[i]
            if sum in hashmap:
                return [i,hashmap[sum]]
                
                
            hashmap[input[i]]=i
            print((hashmap[input[i]]),i)
            

s='abcbcbb'
for i in s:
    print(i)

        


new=Twosum()
print(new.Sum())