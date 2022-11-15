#check_function
def check_guess(guess, answer) :
    #set score variable as global
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower() :
             print ('Correct Answer')
             score = score + 1
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
        
        


#print total score
print('Your score is ' + str(score))






