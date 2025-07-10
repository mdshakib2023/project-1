## Write a program that rotates a list to the left by k positions

def rotates_left(list,k):
    rotates = len(list)
    if rotates == 0:
        return list
    k = k % rotates
    return list[k:] + list[k:]

newlist = [1,2,3,4,5,6] 
k = 2 
listnew = rotates_left(newlist,k)
print("rotstes list:",listnew)  