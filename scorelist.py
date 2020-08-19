scores = []
maxscores = 0
minscores = 100
total = 0
maxname = 0
minname = 0

for i in range(5):
    n = int(input('Grade:'))
    name = input("Enter Name:")
    scores.append(n)
    
    if n > maxscores:
        maxscores = n
        maxname = name
    if n < minscores:
        minscores = n
        minname = name
    total = total + n
        
s = total/len(scores)
print('total:',total)
print('average:',s)
print('Highest score:',maxscores)
print('Lowest score',minscores)
print('Highest name:',maxname)
print('Lowest name:', minname)
