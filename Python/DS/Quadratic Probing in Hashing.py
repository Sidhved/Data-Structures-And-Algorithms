'''Quadratic Probing in Hashing
A technique for collision resolution in hashing tables.
In quadratic probing, the algorithm searched for i^2 position on collision detedtion.
It is more efficient than linear probing since it avoids the clustering problem observed in linear probing
Bast Case: O(1) Worst Case: O(N)
'''

#Function for Quadratic Probing
def QuadProb(hash, hashSize, arr, N):
    for i in range(N):
        hashVal = arr[i] % hashSize
        if hash[hashVal] == -1:     #if empty location
            hash[hashVal] = arr[i]
        else:                       #if occupied slot i.e. collision detected
            k = arr[i]
            for j in range(1, hashSize):    #unlike linear probing, we searh for the entire table here
                hashVal = (k + pow(j, 2)) % hashSize
                if hash[hashVal] == -1:
                    hash[hashVal] = arr[i]
                    break
                else:
                    continue

#Driver Code
if __name__ == "__main__":
    t = int(input())
    while(t>0):
        hashSize = int(input())
        sizeOfArr = int(input())
        arr = list(map(int, input().split()))
        hash = [-1]*hashSize
        #after initialising and declaring values for all the variables, we pass them as parameter to the quadprob function
        QuadProb(hash, hashSize, arr, sizeOfArr)
        for i in hash:
            print(i, end = " ")
        t -= 1