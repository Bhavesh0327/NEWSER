import socket
import mysql.connector
import os
from colorama import Fore, Back, Style
import time
import requests
import json
import sys

categories = [ "bussiness" , "entertainment" , "sports" , "health" , "science" , "technology" , "general" ]

def main():
	#connection with the mysql database
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

	welcome = Fore.WHITE + Back.RED +  "Welcome to NEWSER!!!"
	print(welcome.rjust(57))
	print(Style.RESET_ALL)

	#creating a server to connect with the news file
	buffer = 4096
	port = 3333
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("localhost", port))
	server_socket.listen(10) 			#listen atmost 10 connection at one time
	c, addr = server_socket.accept()	
	
	
	countrycode = (c.recv(buffer)).decode('utf-8')
	time.sleep(0.5)
	category1 = (c.recv(buffer)).decode('utf-8')
	time.sleep(0.5)
	category2 = (c.recv(buffer)).decode('utf-8')
	time.sleep(0.5)
	category3 = (c.recv(buffer)).decode('utf-8')
	news(countrycode , category1 , category2 , category3)

def news(cont , cat1 , cat2 , cat3):
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
		time.sleep(1)
	print("Type exit/quit to exit the app")
	user = (str(input("YOUR INPUT: "))).lower()
	print(user)
	if user == "exit" or user == "quit" :
		print("BYE BYE , HOPE YOU LIKED IT")
		sys.exit()
	elif user == " ":
		time.sleep(300)
		os.system("clear")
		welcome = Fore.WHITE + Back.RED +  "Welcome to NEWSER!!!"
		print(welcome.rjust(57))
		print(Style.RESET_ALL)
		news(cont , user , cat1 , cat2)
	
		


if __name__ == "__main__" :
	main()

