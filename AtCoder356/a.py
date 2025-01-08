N, L, R = map(int, input().split())
ans = [i for i in range(1,N+1)]
p = [i for i in range(R, L-1, -1)]
#print(p)
ans[L-1:R] = p
answer = []
for a in ans:
  a = str(a)
  answer.append(a)
print(" ".join(answer))