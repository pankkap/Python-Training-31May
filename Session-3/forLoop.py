for i in range(1,11):
    print(i)


# 5 10 15 20 25 30 35 40 45 50
# 10 9 8 7 6 5 4 3 2 1
# 2 4 6 8 10 12 14 16 18 20
# 1 3 5 7 9 11 13 15 17 19

# *
# **
# ***
# ****
# *****


for i in range(1,6):
    for k in range(1,i+1):
        print(k, end= "")
    for s in range (9,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        print(j, end= "")
    print("")    