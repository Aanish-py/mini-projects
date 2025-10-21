from cryptography.fernet import Fernet  



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
		
write_key()


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key
key = load_key()
fer = Fernet(key)

def add():
	name = input("Name: ")
	password = input("Password: ")
	

	with open('password.txt','a') as f:
		f.write(f"{name} | {fer.encrypt(password.encode()).decode()}\n")

def view():
	with open('password.txt','r') as f:
		for line in f:
			data = line.rstrip()
			user, pswd = data.split(' | ')
			print(f"Name: {user}, Password: {fer.decrypt(pswd.encode()).decode()}")

while True:
	mode = input("Do you wanna add or view password or quit?: ")

	if mode == 'view':
		view()

	elif mode == 'add':
		add()

	elif mode == 'quit':
		break

	else:
		print("Invalid Input")
		continue
