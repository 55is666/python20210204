#306
j=[]
total=0
avg=0
n=int(input('people'))
for i in range(n):
    name=input('name:')
    score=int(input('score:'))
    score=int(score)
    oneperson=[]
    oneperson.append(name)
    oneperson.append(score)
    j.append(oneperson)
for item in j:
    total=total+item[1]
average=total/n
print('the average is:',average)
high=0
person=''
for item in j:
    if item[1]:
        high=item[1]
        person=item[0]
print(person,'high:',high)
low=100
person=""
for item in j:
    if item[1]<low:
        low=item[1]
        person=item[0]
print(person,'got low point',low)