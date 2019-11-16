"""
                $ PLAYS LOTTERY $
        This program is a kind of lottery that choose between 5 numbers
        with the posibility to get 4 repeated numbers
        
        TO PLAY:
        -Write  number of times to try lucky
        
        the lowest number its more harder..

"""
import math
import random

#variables
lottery_numbers = [0,0,0,0]
win = 0

try:  # if the user don't write a number

    print("how many times you want to play?")
    attempts = int(input())
    print("times played: " + str(attempts))


    #functions
    def per(n,k): # do a permutation (it is to calculate the probability)
        r = n - k
        n = math.factorial(n)
        r = math.factorial(r)
        return n / r 
    
    def chosenNumbers(): # this function choose the random results
        for i in range(4):
            lottery_numbers[i] = random.randint(1,5)
    
    
    
    for i in range(attempts): # just write the results
        print("//")
        chosenNumbers()
        
        print(lottery_numbers)
        
        for i in range(1, 6): # will check if you win
            
            if lottery_numbers.count(i) >= 4:
                win += 1
                print("////!!!!You Wins!!!!!//////")
    
    
    if attempts >= 5: # this is because you cant do a permutiation < attempts numbers
        
        print("you got " + str(win) + " hits of " + str( int( per(attempts, 4) ) ) + " posibilities")
        
        
        if win > 0: # congurlations if you win :]
            print("\nyou are very lucky\n$$  Now you are millionarie  $$ :^)\nYou Won: " + str(win) + " times\n")
            
            win /= per(attempts, 4) * 100
            
            print("probability in total attempts: "+ str(win) +"%")
            
        else:
            print("probability: 0%" ) 
    
    print ("probability of win per attempt: " + str( 1 / math.factorial(4) * 100 ) + "%" )
        
except:
    print("Error: You must to write a 'int' Number")