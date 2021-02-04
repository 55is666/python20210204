#4-2
d={}
while True:
    f=input("enter your options:")
    if f=="6":
        break
    elif f=='1':
        while True:
            gh=input('enter new vocablary(plus 0 to skip)')
            if gh=='0':
                break
            if gh in d:
                print("I'm already here!")
            else:
                m=input("enter its Chinese")
                d[gh]=m
    elif f=='2':
        d1=sorted(d)
        for i in d1:
            print(i,d[i])
    elif f=='3':
        gh=input('enter vocabulary that you want to search:')
        if gh in d:
            print(d[gh])
        else:
            print("I'm not here!")
    elif f=='4':
        er=False
        ch=input("enter Chinese volcabulary that you want to search:")
        for k,v in d.items():
            if ch==v:
                print(ch,"'s English is ",k)
                er=True
        if er==False:
            print("I'm not here!")
    elif f=='5':
        score=0
        print('you have ',len(d),'guestions')
        c=100/len(d)
        for k,v in d.items():
            print(v,':')
            ans=input('')
            if ans==k:
                print ('correct!')
                score=score+c
            else:
                print('wrong')
        print('you got',score,'point')
                
        