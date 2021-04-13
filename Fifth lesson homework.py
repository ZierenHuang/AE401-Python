score = []
name = []
n = input('幾個分數')
n = int(n)

for i in range(n):
    s = input('成績')
    s = float(s)
    na = input('名字')
    score.append(s)
    name.append(na)
    
sum = 0
for i in range(n):
    sum = score[i] + sum

average = sum / n

highest = 0

for i in range(n):
    if highest < score[i]:
        highest = score[i]
        high_index = i
    

low = 100
for i in range(n):
    if low > score[i]:
        low = score[i]
        low_index = i
print('平均', average)
print('最高', highest, '是',name[high_index])

print('最低', low, '是', name[low_index])
 