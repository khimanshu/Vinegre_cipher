#!/usr/bin/python
import string #for string operations
import os #for calling the operating system calls from within the program


# Himanshu Koyalkar
# Date : 03-07-2016
# Class : cs 524- 02
# The program takes key and then gives the user the options to encrypt or decrypt the files of users choice 



while (1):
	print("\t\t Vigenere cipher using Python by Himanshu hk0014@uah.edu")
	alpha = [[0 for x in range(26)] for x in range(26)] #declaring an array for the 2x2 Matrix for deciding the replacement letter 
	letter = string.ascii_lowercase # a string of letters
	print("\n")
	x=0
	y=0
	z=0
	while (x<26):
		for y in range(26):
			alpha[x][y] = letter[(x+y)%26] # initialization of the 2x2 alphabetic array
		x = x+1
	print("\t\tenter the key")
	key = raw_input() # taking the key from the user
	print("\t\tThe entered key is \t\t\t" + "".join(key) + "\n")
	print("\t\t\t\t\tEnter 1 to encrypt and 2 to decrypt files")
	o=raw_input() # option for selecting to encrypt or decrypt
	if o == "1": # encryption option
		print("\t\tEnter the Name of File to Encrypt\n")
		flname = raw_input()  # taking the file input from the user 
		plntext = open(flname,"r")
		message = plntext.read()
		size = len(message)
		message = message.lower() # converting the read string to lower case
		key_cipher = [0 for x in range(size)] # declaring the string for encryption usign the key
		x=0
		k=0
		while(x<size):
			if ord(message[x]) in range(65,122):
				key_cipher[x] = key[(k)%len(key)] # initializing the string for encryptoin using key
				k = k+1
			elif message[x] == " ":
				key_cipher[x] = " "
			else:
				key_cipher[x] = message[x]
			x = x+1
		encrp = [0 for x in range(size)]
		x = 0
		y = 0
		while (x<size): # loop for encrypting the message
			if ord(message[x]) in range (65,122) :
				encrp[x] = alpha[ord(key_cipher[x])-97][ord(message[x])-97] 
			elif message[x] == " ":
				encrp[x] = ' '
			else:
				encrp[x] = message[x]	
			x = x+1
		ecrtx = flname+"_e"
		er = open(ecrtx,"w+")  # opening <filename>_e file to write encrypted text
		er.write("".join(encrp)) # writing the string into the file
		plntext.close()
		er.close()  # closign the file
		print("\n\t\t Encryption file created")
	if o == "2":  # option for decryption
		print("\t\tEnter the Name of File to Decrypt\n")
		flname = raw_input()   # taking the file name from the user
		cprtext = open(flname,"r")  # opening the file
		message = cprtext.read()  # reading encrypted content
		message = message.lower()
		size = len(message)
		key_cipher = [0 for x in range(size)] # declaring a string used for decryption using the key
		x=0
		k=0
		while(x<size):  # initializing the string used for decryption using the key
			if ord(message[x]) in range(65,123):   
				key_cipher[x] = key[(k)%len(key)]
				k = k+1
			elif message[x] == " ":
				key_cipher[x] = " "
			else:
				key_cipher[x] = message[x]				
			x = x+1
		decrp = [0 for x in range(size)]
		dectx = flname+"_d" 
		x=0
		l=0
		while (x<size):  # decrypting the message
			if ord(message[x]) in range (65,123):
				k = ord(key_cipher[x])-97
				l = alpha[k].index(message[x])
				decrp[x] = letter[l]	
			elif message[x] == " ":
				decrp[x] = " "
			else:
				decrp[x] = message[x]
			x = x + 1
		#print("\t\tDecryted text is \n\t\t"+"".join(decrp))
		dec = open(dectx,"w+")
		dec.write("".join(decrp))  # writng to file with <filename>_d name
		cprtext.close()
		dec.close()
		print("\n\t\t Decryption file created")
	print("\t\tEnter ctrl+c to exit and ENTER to continue")
	c = raw_input()
	os.system('clear')
