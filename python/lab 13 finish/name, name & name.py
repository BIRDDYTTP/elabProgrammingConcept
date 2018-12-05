def namelist(names):
    count = 1
    a = ''
    for x in names:
        if count < len(names)-1:
            a += x+', '
        elif count == len(names)-1:
            a += x+' & '
        else:
            a += x
        count += 1
    return a
print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Peter']) )
print( namelist([]) == '' )