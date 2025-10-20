print("Welcome to Quiz game")

playing = input("Do you wanna Play the Quiz? ")
if playing.lower() != 'yes':
	quit()


print("Okay Lets play!")

score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
	print("correct")
	score += 1

else:
	print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
	print("correct")
	score += 1

else:
	print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
	print("correct")
	score += 1

else:
	print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
	print("correct")
	score += 1

else:
	print("Incorrect")

print(f"You score is {score}")
