import random

print("Welcome to The Rock Paper and Scissors Game!")

options=['rock','paper','scissors']
comp_win = 0;
user_win = 0;

while True:
	user_input = input("Choose Rock,Paper or Scissors or Q to quit: ").lower()
	comp_pick_num=random.randint(0,2)
	comp_pick = options[comp_pick_num]

	if user_input == 'q':
		break
	
	elif user_input not in options:
		print("Wrong Input")
		continue

	elif user_input == 'rock' and comp_pick == 'scissors':
		print(f"Computer Chose {comp_pick}"+"\nCongrats! You won")
		user_win+=1

	elif user_input == 'paper' and comp_pick == 'rock':
		print(f"Computer Chose {comp_pick}"+"\nCongrats! You won")
		user_win+=1

	elif user_input == 'scissors' and comp_pick == 'paper':
		print(f"Computer Chose {comp_pick}"+"\nCongrats! You won")
		user_win+=1

	else:
		print(f"Computer Chose {comp_pick}"+"\nYou lost")
		comp_win += 1

print(f"\nYou won {user_win} times.")
print(f"Computer won {comp_win} times")
print("Thanks for playing!")
