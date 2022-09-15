
MyList = list(range(1, 101))
NewList = []
index = 0
while index < len(MyList):
    if MyList[index] % 7 == 0 and MyList[index] % 5 != 0:
        NewList.append(MyList[index])
    index += 1
 
print(NewList)
