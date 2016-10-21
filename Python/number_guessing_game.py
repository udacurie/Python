"""
Created on Feb 1,2016, 4.30 AEDT
@author: udacurie
@email: udacurie@gmail.com

=====================
  Function usage
=====================  
This code is a number guessing game which accepts an integer between 1-100 as input guess,
compares to a random number in that range and indicates if the guess is correct, high, low, repeat or invalid.
If the guess is correct, it gives the number of guesses takne (minus the repeated guesses).

Initial call via:
>>> print number_guessing_game(user_input)
The function then implicitly ietrates requesting player more guesses as required

"""

#!/usr/bin/env python 2.7.10

def number_guessing_game(user_ip):
    # Initialise
    a = 1     # 1st number of range
    b = 100   # last number of range
    s_guess=0 #single guess
    d_guess=0 #duplicate guess
    guess = list() #list of user inputs
    play = True
    valid = True

    # Step1: generate a random integer from 1-100
    import random
    rnum = (random.randint(a,b)) 
    guess.append(user_ip)

    #Step 2:Loop untill guess is correct 
    while play:
        
        #Step 2a: if guess is correct, print output
        if user_ip == rnum:
            result = "Congratulations..you psychic you..!! You took "
            s_guess = s_guess+1
            msg = result + str(s_guess) + " guess(es)."
            break
        
        #Step 2b: if guess is incorrect, guide player of proximity
        if user_ip != rnum:
            if rnum < user_ip:
                result= "Number too high"
            elif rnum > user_ip:
                result= "Number too low"
                
         #Step 2b1: advise player if guess is repeated
            if len(guess)>1:
                if guess.count(user_ip)>1:
                    d_guess = d_guess+1
                    print result + " and has been guessed before. Try again"
                else:
                    s_guess = s_guess+1
                    print result + ". Try again "
            elif len(guess)==1:
                s_guess = s_guess+1
                print result + ". Try again "
                
            #Step 2c: if guess is incorrect, ask player to guess again
            #Also check if number is within range  
            while valid:
                n=int(raw_input("Please enter another number between "+str(a)+" and "+str(b)+":"))
                if(n not in range(a,b+1)):
                    print "Invalid number. Please choose between",str(a),"and",str(b)
                else:
                    break
                
            #Step 2d: append the new guess to the list for next iteration
            user_ip = n
            guess.append(user_ip)
            
    return msg
    
   
