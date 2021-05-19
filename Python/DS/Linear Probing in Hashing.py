'''Linear Probing in Hashing
A technique for resolving hash collision of values in hash function. It comes under open addressing.
In this mapping, each cell of the hash table stores single key-value pair
When collision is observed at any particular cell of the hash table, i.e. the key to be addressed is pre occupied,
The linear probing algorithm searches for the next closest free index and allocates the value to that index
Best Case = O(1) Worst Case = O(n)
'''

#Function for linear probing:
def linearProb(hash, hashSize, arr, sizeOfArray):
    for i in arr:
        keySpace = i % hashSize     #determining table index
        if hash[keySpace] == -1:    #-1 determines unoccupied or empty slot
            hash[keySpace] = i
        else:                       #if occupied by some i
            for j in range(keySpace+1, keySpace+hashSize):  #searhing for next empty slot
                j = j % hashSize
                if hash[j] == -1:
                    hash[j] = i
                    break

#driver Code
if __name__ == "__main__":
    t = int(input())
    while(t>0):
        hashSize = int(input())
        sizeOfArray = int(input())
        arr = list(map(int, input().split()))
        hash = [-1] * hashSize
        #after initializing all the variables and setting values, we send them as a parameter to our linear probbing function
        linearProb(hash, hashSize, arr, sizeOfArray)
        for i in hash:
            print(i, end =" ")

        t -= 1
