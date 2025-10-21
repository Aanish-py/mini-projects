import random
while True:
    print("Welcome to Number Guessing Game\n")
    top_of_range = input("Select The Highest possible Number: ")
    
    randnum = random.randrange(1,int(top_of_range))
    guess = 1;
    
    while True:
    	user_num = input("Guess The Number: ")
    	if user_num.isdigit():
    	    user_num = int(user_num)
    	    if user_num == randnum:
    	        break
    	    elif user_num > randnum:
    	        print("Go Lower")
    	        guess+=1
    	        continue
    	    elif user_num < randnum:
    	        print("Go Higher")
    	        guess+=1
    	        continue
    	else:
    	    print("Please Type a number")
    	    continue
    
    	    
    print(f"\nThe number was {randnum}")	  
    print(f"Congrats You Guessed it in {guess} tries")
    again = input("Do You wanna Play again?: ")
    if again == 'yes':
        continue
    else:
        print("Thanks For Playing")
        break
