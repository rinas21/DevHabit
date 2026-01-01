numarray = [1,2,3,2,4,5,1,3]

def duplicatenum(numarray):
    duplicates=[]
    for i in numarray:
        if numarray.count(i)>1 and i not in duplicates:
            duplicates.append(i)
    return duplicates
    print(duplicates)
duplicatenum(numarray)
print(duplicatenum(numarray))