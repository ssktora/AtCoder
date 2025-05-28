N = int(input())
ans = []
r = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111, 11111111111, 111111111111]
for i in range(len(r)):
    for j in range(i+1):
        for k in range(j+1):
            p = r[i]+r[j]+r[k]
            ans.append(p)
print(ans[N-1])

    
        
