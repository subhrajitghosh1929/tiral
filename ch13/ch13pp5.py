lst = [(103 , 'Ritika' , 3001),(104 ,'john',2819),(101,'Razai',3451),(105,'Tarandeep',2971)]
for i in range( len( lst ) - 1 ):
    for j in range( len ( lst ) - 1 ):
        if lst [ j ] [ 2 ] < lst [ j + 1 ] [ 2 ] :
            lst [ j ] , lst [ j + 1 ] = lst [ j + 1 ] , lst [ j ]
print(lst)
