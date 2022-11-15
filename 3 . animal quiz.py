#check_function
def check_guess(guess, answer) :
    #set score variable as global
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower() :
             print ('Correct Answer')
             score = score + 3 - attempt
             still_guessing = False

        else :
            if attempt < 2 :
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer is ' + answer)

       
    

score = 0

print ('Guess the Animal !')
#question 1
guess1 = input('Which bear lives at the north pole ? ')
check_guess(guess1, 'polar bear')
# question 2
guess2 = input('Which is the fastest land animal ? ')
check_guess(guess2, 'cheetah')
#question 3
guess3 = input ('Which is the largest Animal ? ')
check_guess(guess3, 'blue whale')
#question 4
guess4 = input('Which one of these is a fish ?\n A)Whale\n B)Dolphin\n C)Shark\n D)Squid\n Type A, B, C, D ')
check_guess(guess4, 'c')
        
        


#print total score
print('Your score is ' + str(score))






