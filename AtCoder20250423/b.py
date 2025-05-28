S = input()
T = input()
con = {"AC", "AD", "BD", "BE", "CE", "CA", "DA", "DB", "EB", "EC"}
if S in con and T in con:
    print("Yes")
elif S not in con and T not in con:
    print("Yes")
else:
    print("No")