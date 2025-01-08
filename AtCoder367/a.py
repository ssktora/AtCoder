A, B, C = map(int, input().split())
if B <= A <= C:
    print("No")
elif B <= C <= A:
    print("Yes")
elif B <= A <= 23 and 0 <= C <= B:
    print("No")
elif B <=  23 and 0 <= A <= C <= B:
    print("No")
else:
    print("Yes")