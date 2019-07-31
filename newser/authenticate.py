import socket
import mysql.connector
import time
import getpass
import sys
from country import*

i=1
categories = [ "bussiness" , "entertainment" , "sports" , "health" , "science" , "technology" , "general" ]


mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="igj3211822njdc4j"
)
mycursor = mydb.cursor()
mycursor.execute("USE user_login")

buffer = 4096
host='localhost'
port = 3333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

sign = (input("NEW OR OLD USER:")).lower()
def categoryList ( category ) :
	if category not in categories:
		print("YOU SEEM TO POSSESS SOME DIFFERENT INTERESTS SIR, KINDLY CHOOSE ANY ONE OF THE ABOVE ONLY PLEASE")
		category = (str(input("YOUR CHOICE PLEASE:-"))).lower()
		categoryList(category)
		return category
	else:
		pass
def password():
	global passwd
	global confirm_passwd
	passwd = getpass.getpass("PASSWORD: ")
	confirm_passwd = getpass.getpass("CONFIRM PASSWORD: ")

def checkemail(mail):
	mycursor.execute("SELECT* FROM authentication where email_id = %s" , (mail , ))
	result = mycursor.fetchall()
	if (result):
		print("EMAIL ALREADY TAKEN PLEASE ENTER A NEW EMAIL ID PLEASE!!!")
		mail = str(input("EMAIL-ID: "))
		checkemail(mail)
	else:
		pass

def authenticate( mailID , password , index):
	mycursor.execute("SELECT* FROM authentication where email_id = %s and password = %s" , (mailID , password ))
	result = mycursor.fetchall()
	if (result):
		return
	else:
		print("IT SEEMS YOU ENTERED WRONG CREDENTIALS")
		
		if (index == 0):
			print("SORRY YOU ARE NOT ALLOWED TO USE THIS CODE NOW")
			sys.exit()
		else:
			index-=1
			print("YOU HAVE " + str(index) + " CHANCES LEFT , TRY AGAIN" )
			mailID =  str(input("EMAIL-ID: "))
			password = getpass.getpass("PASSWORD: ")
			authenticate(mailID , password , index)


if sign == "new":
	name = str(input("NAME: "))
	email = str(input("EMAIL-ID: "))
	checkemail(email)
	password()
	if passwd != confirm_passwd:
		print("PASSWORDS DON'T MATCH ENTER AGAIN")
		password()
	countryname = (str(input("FULL NAME OF YOUR COUNTRY PLEASE: "))).upper()
	countrycode = country.country[countryname]
	print("CHOOSE ANY 3 INTERESTS OF YOUR CHOICE FROM THE FOLLOWING")
	for cate in categories:
		print(str(i) + ":" + cate.upper())
		i=i+1

	category1 = (str(input("1st CHOICE:-"))).lower()
	categoryList(category1)
	category2 = (str(input("2nd CHOICE:-"))).lower()
	categoryList(category2)
	category3 = (str(input("3rd CHOICE:-"))).lower()
	categoryList(category3)
	
	mycursor.execute("INSERT INTO authentication (email_id , password , Name , country , category1 , category2 , category3) values (%s ,%s ,%s ,%s ,%s ,%s ,%s )" , ( email , passwd , name , countrycode , category1, category2, category3))
	mydb.commit()
	s.send(countrycode.encode())
	
elif (sign == "old"):
	email = str(input("EMAIL-ID: "))
	passwd = getpass.getpass("PASSWORD: ") 
	j=5
	authenticate(email , passwd , j)
	mycursor.execute("SELECT* FROM authentication where email_id = %s and password =%s" , (email , passwd))
	results = mycursor.fetchall()
	for x in results:
		s.send(x[3].encode('utf-8'))
		time.sleep(0.5)
		s.send(x[4].encode('utf-8'))
		time.sleep(0.5)
		s.send(x[5].encode('utf-8'))
		time.sleep(0.5)
		s.send(x[6].encode('utf-8'))
		time.sleep(0.5)
		
else:
	print("WRONG INPUT")


