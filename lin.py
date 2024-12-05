pos = 0
def search(list,n):
    for i in list:
        if i == n:
            globals()['pos']= list.index(i)
            return True
    else :
            return False

list = [2,7,5,3,0]
n = 3
if search(list,n):
    print("found at ",pos +1)
else :
    print("not found")