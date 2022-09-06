# Hash Table - Return 1st Recurring Number

# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]
# it should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1

# Given an array = [2,3,4,5]
# it should return undefined

# arrInput = [2,5,1,2,3,5,1,2,4]
# arrInput = [2,1,1,2,3,5,1,2,4]
arrInput = [2, 3, 4, 5]
uniqueArr = []

if arrInput == list(set(arrInput)):
    print("undefined")
else:
    for i in arrInput:
        if i in uniqueArr:
            print(i)
            break
        else:
            uniqueArr.append(i)
