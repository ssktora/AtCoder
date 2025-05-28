p,q = input().split()
grid = [0,3,4,8,9,14,23]
p_dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}
print(abs(grid[p_dic[p]]-grid[p_dic[q]]))