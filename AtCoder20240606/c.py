N = int(input())
a_list = []
for i in range(N):
    a = int(input())
    a_list.append(a)
sorted_list = sorted(a_list)
for i in range(N):
    p = a_list[i]
    if p == sorted_list[-1]:
        print(sorted_list[-2])
    else:
        print(sorted_list[-1])