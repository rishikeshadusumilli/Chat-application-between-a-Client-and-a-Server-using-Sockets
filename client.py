#Client Program

import socket							#Importing to implement commmand line arguments
import sys							#Importing to implent socket programming
import os							#Importing to implement file handling


#############################IP and Port information#######################

def commandArg():						#Function to handle command line arguments to take input of port
	if len(sys.argv) != 3:					#If number of arguments provided is less than 2 then it will error out
		print("Enter IP address and Port")
		sys.exit()
	return sys.argv[1], sys.argv[2]

	
##############################################################################

################################Put Function##################################
def putFi(COMMAND, fileI):					#Function to send file from client to server
	try:							#Checking if any exception raises to correctly catch it

		if(os.path.isfile(fileI)):			#Check if file is present in current directory or error out
         		file1=open(fileI, "rb")			#Open file in read, binary mode to perform operations
						
			for f1msg2 in file1:			#Iterate through contents of file and take each line as packet
			
				encodedMsg=COMMAND + "???" + fileI + "???" + f1msg2       #Create a message containg message and command seperated by delimiter
				propMsg="Message???" + encodedMsg
		       		s.sendto(propMsg, (host, port))		#Sending message to server
				
				s.settimeout(10)			#Client will time out if the server does not respond
                		
				data, servAddr = s.recvfrom(1024)	#Receive acknowledgement from server
                			
				print("Server reply : " +data)

			
			file1.close()					#Close file upon completion of operation
		else:
			
               		errorMsg = "Inproper file name or file does not exist"	#Error message if file does not exist
               		print(errorMsg) 
	
	except socket.timeout, msg:					#Catching socket.timeout exception if server timeouts and if client is waiting
        	print("Receiver "+str(msg))
        	
	
##############################################################################

###################################Get Function###############################
def getFi(COMMAND, fileI):					#Function to send command to server and receive file from server 
        try:							#Checking for any exceptions to catch them
			
        	propMsg="???" + COMMAND + "???" + fileI		#Creating message containg command and encoded file seperated by delimiter
        	s.sendto(propMsg, (host, port))
		
		s.settimeout(10)				#Client will time out if the server does not respond
		
		encodedMsg, servAddr = s.recvfrom(1024)		#receiving file from user upon request
		splitMsg=encodedMsg.split("???")		#Extracting message and command due to delimeter encoding
		if(splitMsg[0]=="Message"):			#If no error and if file present, we will proceed
			while(encodedMsg != "done"):		#If file is not completely delivered, then proceed
				splitMsg=encodedMsg.split("???")
	
				extractedMsg=splitMsg[3]	#Extracting message from server message by splitting depending on delimeter
				f1msg1=open("received_"+fileI, "ab")	#Writing contents to new file at client in append mode
        			f1msg1.write(extractedMsg)
        			f1msg1.close()				#closing file after append/write operation
				
				backMsg = "Thanks"			#Send acknowledgement back to server after receiving packets
	        		s.sendto(backMsg, servAddr)
				
				encodedMsg, servAddr = s.recvfrom(1024)	#Receiving next packet

		elif(splitMsg[0]=="Error"):			#If server does not contain file, then error message will be received from server
           		print 'Server reply : ' +splitMsg[1]

			
        except socket.timeout, msg:
        	print("Receiver "+str(msg))
        
	
###########################################################################

####################################List Function##########################
def listOption(COMMAND):					#Function to send contents of server
	try:							#Checking for any exceptions to catch them			
                propMsg="???" + COMMAND + "???" 		#Sending command of client and message encoded with delimeter to secure information
                s.sendto(propMsg, (host, port))	
                
		s.settimeout(10)				#Client will time out if the server does not respond	
		
		data, servAddr = s.recvfrom(1024)		#Receiving contents of server folder
                print 'Server reply : ' +data
                
		msg1="Thanks"					#Send acknowledgement back to server after receiving packets
                s.sendto(msg1,servAddr)

        except socket.timeout, msg:				#Catching socket.timeout exception if server timeouts and if client is waiting
                print("Receiver "+str(msg))

###########################################################################

##########################Exit Function####################################
def exitOption():						#Function to send command to exit the server program
	try:							#Checking for any exceptions to catch them			
                propMsg="???" + COMMAND + "???"			#Sending command of client and message encoded with delimeter to secure information
                s.sendto(propMsg, (host, port))

		sys,exit()					#Exiting the client upon exit of client

        except socket.timeout, msg:				#Catching socket.timeout exception if server timeouts and if client is waiting
                print("Receiver "+str(msg))
	
##########################################################################

########################Other Commands####################################
def otherC(COMMAND3):
	try:							#Checking for any exceptions to catch them
		propMsg="???" + COMMAND + "???"			#Sending command of client and message encoded with delimeter to secure information
		s.sendto(propMsg, (host, port))
			
		s.settimeout(10)				#Client will time out if the server does not respond	
                data, servAddr = s.recvfrom(1024)		#Receive error message from server
                print 'Server reply : ' +data

	except socket.timeout, msg:				#Catching socket.timeout exception if server timeouts and if client is waiting
		print("Receiver "+str(msg))

###########################################################################

if __name__ == '__main__':					#Main function


	host, port1=commandArg()				#Take port and IP as command line arguments from user
	port=int(port1)						#Convert port to int type
	if(port < 5000):					#Accept only port inputs greated than 5000
		print("Enter port number greater than 5000")
		sys.exit()					


	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#Created socket for UDP protocol
	except socket.error:						#Catch socket.error, if socket failed to create
		print "Failed to create socket"
		sys.exit()


	while(1) :							#Client and server stays in loop during converstaion
		print("Please enter the command with spaces:\nThe options presented to the user are:\nget[file_name]\nput[file_name]\nlist\nexit")
		COMMAND1 = raw_input("Input: ")				#Take input of command from user
		COMMAND3 = COMMAND1.lower()				#Input should always be in lowercase
		COMMAND2 = COMMAND3.split()				#Split to extract command and filename from user
		COMMAND = COMMAND2[0]					#Storing command only from user input

		if(COMMAND3=="list"):					#Select particular function depending on command input
			listOption(COMMAND)
		elif(COMMAND3=="exit"):
			exitOption()
		elif(COMMAND==("put")):
			try:
				if(COMMAND2[1] != ""):			#Check if filename is provided with command as input
					fileI=COMMAND2[1]
				else:
					print("Please provide proper filename")
					continue
			except:		
				print("Please provide proper filename")		
				continue
			putFi(COMMAND, fileI)
		
		elif(COMMAND==("get")):
			try:
				if(COMMAND2[1] != ""):	
					fileI=COMMAND2[1]	
				else:
					print("Enter Proper filename")
					continue
			except:
				print("Enter proper filename")
				continue
			
			getFi(COMMAND, fileI)
		else:
			otherC(COMMAND3)
