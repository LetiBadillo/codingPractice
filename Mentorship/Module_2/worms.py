import math

"""
-----------------------------------------------------------------------------------------------------

    B. Worms
    It is lunch time for Mole. His friend, Marmot, prepared him a nice game for lunch.

    Marmot brought Mole n ordered piles of worms such that i-th pile contains ai worms. He labeled all these worms with consecutive integers: worms in first pile are labeled with numbers 1 to a1, worms in second pile are labeled with numbers a1 + 1 to a1 + a2 and so on. See the example for a better understanding.

    Mole can't eat all the worms (Marmot brought a lot) and, as we all know, Mole is blind, so Marmot tells him the labels of the best juicy worms. Marmot will only give Mole a worm if Mole says correctly in which pile this worm is contained.

    Poor Mole asks for your help. For all juicy worms said by Marmot, tell Mole the correct answers.

    Input:
    2 7 3 4 9
    1 25 11

    Output
    1
    5
    3

-----------------------------------------------------------------------------------------------------


""" 
def main():
    #Get piles
    piles = input()
    arrayPiles = [int(x) for x in piles.split()] 
    
    #Get juicy worms
    juicyWorms = input()
    juicyWormsArray = [int(x) for x in juicyWorms.split()]

    print("Output:")
    #Calculate ranges
    ranges = []
    left = 1
    right = 0
    for pile in arrayPiles:
        right = right + pile
        ranges.append([left, right])
        left = right+1

    #For each worm, search if it's between a range
    for worm in juicyWormsArray:
        t = 0
        l = len(ranges)-1
        found = False
        #Binary search to find if worm is between each range
        while(t <= l):
            m = math.ceil((t+l)/2)
            if(worm >= ranges[m][0] and worm <= ranges[m][1]):
                found = True
                print(m+1)
                break
            elif(worm > ranges[m][1]):
                t = m + 1
            elif(worm < ranges[m][0]):
                l = m - 1
        if(not found):
            print(-1)
    
        
main()

