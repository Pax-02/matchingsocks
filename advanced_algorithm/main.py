
def pairSocks(arr):
    # represents number of pairs and we are starting with o pairs
    p = 0
    # b is a dictionary to help us store each element uniquely and the number of times it occured
    b = {}
    # loop into the array
    for i in arr:
        # x is the one that stores the values of counts of an element in the array
        x = arr.count(i)
        # Store the element as a key and the count as values in the dictionary
        b[i] = x
    # loop in all the element in the dictionary
    for i in b:
        # getting the values in the dictionary
        x = b.get(i)
        # flooe divide the count of each element to know how many pairs are in and then add up pairs
        p += (x // 2)

    return p

array1 = [1,2,1,0,3,4,4,5,6,7,7,1,11,11,32,43,43,32,45,65,76,45,22,21,25,22,67,67,99,99]

print ("Number of socks in Array 1 is "+str(len(array1))+" and "+ str(pairSocks(array1))+" Pairs of socks ")

array2 = [76,75,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,23,43,23,21,99,99,100,100,66,77,88,44]
print ("Number of socks in Array 2 is "+str(len(array2))+" and "+ str(pairSocks(array2))+" Pairs of socks ")