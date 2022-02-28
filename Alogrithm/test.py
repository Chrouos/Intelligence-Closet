from tkinter.tix import MAX


li1 = [5, 8]
li2 = [3, 4]

bestScore = 40
nowScore = -5
diff = bestScore - nowScore  # 30

min = 999
bestScpre = 0
for li in li1:
    tempScore = abs(diff - li)
    print('T: {} = {} - {}'.format(tempScore, diff, li))
    if tempScore < min:
        min = tempScore
        bestScore = li

print(bestScore, min)
