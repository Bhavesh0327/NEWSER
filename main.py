import mysql.connector
import getpass
import sys
import tqdm
import os
import requests
import json
from colorama import Fore, Back, Style 
from utility import *
import time


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="igj3211822njdc4j"
)

mycursor = mydb.cursor()

try:
	mycursor.execute("CREATE DATABASE user_login")
except:
	pass
mycursor.execute("USE user_login")
try:
	mycursor.execute("CREATE TABLE authentication ( email_id VARCHAR(255), password VARCHAR(255) , Name VARCHAR(255) ,country VARCHAR(255) , category1 VARCHAR(255) ,category2 VARCHAR(255), category3 VARCHAR(255))")
except:
	pass

i=1
categories = [ "bussiness" , "entertainment" , "sports" , "health" , "science" , "technology" , "general" ]

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

def main(cont , cat1 , cat2 , cat3):
	print(Fore.BLACK + Back.YELLOW+ " THE TOP NEWS HEADLINES FOR TODAY ARE AS FOLLOWS (the news automatically updates after every 5 minutes)")
	print(Fore.BLACK + Back.YELLOW+ " Right click over the blue lines to open full news ")
	categories = (cat1 , cat2 , cat3)
	for x in categories:
		url = ('https://newsapi.org/v2/top-headlines?'
	       'country='+cont+'&'
	       'apiKey=c81dbd34c8494baa93c09fac69c934a8&'
	       'category='+x)
		response = requests.get(url)
		data = json.loads(response.text)
		news_list = data['articles']
		for news in news_list:
			if news['description'] is None:
				continue
			else:
				print(Fore.RED + Back.WHITE + news['title'] , end='')
				print(Style.RESET_ALL) 
				if news['author'] is None:
					print(Fore.YELLOW + news['description'])
					print(Fore.BLACK + news['url'] + "\n")
				else:
					print(Fore.YELLOW + news['description'] + " - by " + news['author'] + "\n")
		time.sleep(2)
	time.sleep(180)
	os.system("clear")
	main(cont , cat1 , cat2 , cat3)
	


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
	os.system("clear")
	main( countrycode , category1 , category2 , category3)
	
elif (sign == "old"):
	email = str(input("EMAIL-ID: "))
	passwd = getpass.getpass("PASSWORD: ") 
	j=5
	authenticate(email , passwd , j)
	mycursor.execute("SELECT* FROM authentication where email_id = %s and password =%s" , (email , passwd))
	results = mycursor.fetchall()
	os.system("clear")
	for x in results:
		main(x[3] , x[4] , x[5] , x[6])
		
else:
	print("WRONG INPUT")





	
	
	

