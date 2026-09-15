for a in range(1,21):
    mersnum=2**a-1
    mid=int(mersnum/2)
    for b in range(2,mid):
        if mersnum % b ==0:
            print(mersnum)
            break
    else:
        print(mersnum,"\tprime")
