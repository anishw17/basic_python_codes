import time
list ={'ROLL NO':'NAME'}
while True:
    print('         MENU BAR\n Enter 1- to add name in list\n Enter 2- to remove name form list.\n Enter 3- to see list\n Enter 4- to search list')
    uip = int(input(' Enter number :'))
    time.sleep(1)
    if uip ==1:
        r= int(input('ENTER THE ROLL NO :'))
        time.sleep(1)
        aip = str(input('ENTER THE NAME TO BE ADDED :'))
        time.sleep(1)
        list.update({r:aip})
        print('ADDED TO LIST!')
    elif uip==2:
        rip = int(input('ENTER THE ROLL NO  TO BE REMOVED :'))
        time.sleep(1)
        list.pop(rip)
        print('REMOVED FROM LIST!')
    elif uip ==3:
        for k,v in list.items():
            print(k,v)
    elif uip ==4:
        s = int(input('ENTER THE ROLL NO TO SEARCH :'))
        time.sleep(1)
        if s in list :
            print(list.get(s))
        else:
            print('ROLL NO DOES NOT EXISTS!')
    else:
        print('ERROR! (enter the valid option)')