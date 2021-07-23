def servingtime(l, n):
    if n == 1:
        return sum(l)
    elif len(l) <= n:
        return max(l)

    dict = {}
    for i in range(n):
        dict[i] = l.pop(0)

    temp = 0
    while any(dict.values()):
        for r in dict.copy():

            dict[r] -= 1
            if dict[r] <= 0:
                try:
                    dict[r] = l.pop(0)
                except IndexError:
                    dict[r] = 0

        temp += 1

    return temp


l = [5, 1, 4, 6, 6, 3, 7]
n = 6

print(servingtime(l, n))
