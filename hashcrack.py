import hashlib
flag = 0

hash_bar = input("Enter mdf hash: ")

wordlist = input("Enter your file: ")

try:
	open_file = open(wordlist , ''r'')
	
except:
	print("No file found")
	quite()
	
for word in open_file:
	enc_word = word.encode('utf-8')
	digest = hashlib.md5(enc_word.strip()).hexdigest()
	if digest == hash_bar:
		
		print("Password found")
		print("Password is  " + word)
		flag = 1
		break														
					
	if flag == 0:
		print("Password not found")												