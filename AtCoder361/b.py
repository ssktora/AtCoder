A = list(map(int, input().split()))
B = list(map(int, input().split()))
b_list = [(B[0], B[1], B[2]),
          (B[3], B[1], B[2]),
          (B[0], B[4], B[2]),
          (B[0], B[1], B[5]),
          (B[0], B[4], B[5]),
          (B[3], B[1], B[5]),
          (B[3], B[4], B[2]),
          (B[3], B[4], B[5])
          ]
x_min, x_max = min(A[0], A[3]), max(A[0], A[3])
y_min, y_max = min(A[1], A[4]), max(A[1], A[4])
z_min, z_max = min(A[2], A[5]), max(A[2], A[5])

frag = True
for b in b_list:
    if x_min < b[0] < x_max and y_min < b[1] < y_max and z_min < b[2] < z_max:
        print("Yes")
        frag = False
        break
if frag:
    print("No")