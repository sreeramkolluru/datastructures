def createdll():
    a=0
    print ("enter the list of elements comma separated")
    a=input().split(',')
    print (a)
    linkedlist=[]
    prev=''
    it=iter(a)
    next(it)
    for dictdata in a:
        try:

            key=['prev','dictdata','nextval']
            value=[prev,dictdata,next(it)]
            linkedlist.append(dict(zip(key,value)))
            prev=dictdata

        except Exception:

            key = ['prev', 'dictdata', 'nextval']
            value = [prev, dictdata, None]
            linkedlist.append(dict(zip(key, value)))
            prev = dictdata

    print(linkedlist)

createdll();