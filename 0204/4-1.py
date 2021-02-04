#4-1
sell=0
cus=[]
while True:
    ll=int(input('功能選項:'))
    if ll==6:
        break
    elif ll==1:
        num=int(input('apple count:'))
        cost=int(input('apple cost:'))
        applen=int(input('成本:'))
        print('目前成本:',applen*num)
    elif ll==2:
        applein=int(input('apple in:'))
        num=num+applein
        print('apple count:',num)
        print('目前成本:',applen*num)
    elif ll ==3:
        appleout=int(input('sell count:'))
        print('應付',appleout*cost,'元')
        num=num-appleout
        sell=sell+appleout
        print('apple count:',num,'顆')
        cus.append(appleout)
    elif ll==4:
        for i in range(len(cus)):
            print(cus[i],'顆')
        total=sell*cost
        print('sell count:',sell)
        print('營業額',total,'元')
        applen=num*applen
        print('賺了',total-applen,'dollers')
    elif ll==5:
        print('剩',num,'顆')
    else:
        print('errorrrrrerrrrrreroorkokrofkodfkoeklsfmksmfk')
            
