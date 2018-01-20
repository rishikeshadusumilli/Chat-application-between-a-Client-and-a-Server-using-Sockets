#Server Program

import sys 					#Importing to implement commmand line arguments 
import socket					#Importing to implent socket programming
import os					#Importing to implement file handling

#################################IP and Port Information######################
def commandArg():				#Function to handle command line arguments to take input of port
	if len(sys.argv) != 2:			#If number of arguments provided is less than 1 then it will error out
		print("Enter port to use")
		quit()
	return sys.argv[1]

###############################################################################

#############################Put Function######################################
def putFi(COMMAND, fileI, clientAddr):		#Function to receive file from client
	
        print("Client Command: "+COMMAND+"["+fileI+"]")
	encodedMsg=splitMsg[3]			#Extract file encoded using message from client
       	f1msg1=open(fileI, "ab")		#Open file in append, binary mode to write/append
        f1msg1.write(encodedMsg)		#Append the contents to file
        f1msg1.close()				#Close file after operation

        sendMsg = "Thanks"			#Convey message is received to sender
        s.sendto(sendMsg, clientAddr)		#Send Thanks message to sender

###############################################################################

################################Get Function###################################
def getFi(COMMAND, fileI, clientAddr):		#Function to receive command and send file to client
	print("Client Command: "+COMMAND+"["+fileI+"]")

	if(os.path.isfile(fileI)):		#If file is present only then proceed
	       	file1=open(fileI, "rb")		#Open file in read, binary mode
				
		for f1msg2 in file1:		#Iterating through file to send each line as packets to user
			encodedMsg=COMMAND + "???" + fileI + "???" + f1msg2	#Sending command of client and message encoded with delimeter to secure information
			propMsg= "Message???" + encodedMsg	
               		s.sendto(propMsg, clientAddr)	#Sending file and command to client
			
			data, clientAddr = s.recvfrom(1024)	#Receive acknowledgement from client after receiving file
          		print ("Client reply : " +data)
				
		s.sendto("done", clientAddr)			#Send the end of file to client to indicate file transfer completion
		file1.close()					#Close file after operation done
	else:
	     	errorMsg = "Error???Improper file name or file does not exist???"	#If file does not exist at server side, send error to client
        	s.sendto(errorMsg, clientAddr)
                

##############################################################################

#################################list Function################################
def listOption(COMMAND, clientAddr):		#Function to send contents of server
        print("Client Command: "+COMMAND)
	
	statusMsg = []				#Defining empty list to later append contents before sending to client
	for file in os.listdir(os.curdir):	#Check files in current directory
		if((file.endswith(".py"))):	#If file end with .py then ignore and continue searching in current directory
			continue
		elif(file.endswith(".txt")or (file.endswith(".jpg"))):	#If files are ending with .jpg or .txt, then add them to list
			statusMsg.append(file)		#Append file name to list
	statusMsg1=" ".join(statusMsg)			#Convert the entire list to string for the purpose of sending to client
   	s.sendto(statusMsg1, clientAddr)

        msg1, clientAddr = s.recvfrom(1024)		#Receive client acknowledgement 
        print("Client reply: "+ msg1)

##############################################################################

###############################Exit Function##################################
def exitOption():				#Function to exit upon request by client
	
	s.close()				#Close socket after operation if requested
	sys.exit()

##############################################################################

###############################Other Commands Function########################
def otherC(COMMAND, clientAddr):		#Function to return error message of unknown commands to client

	statusMsg1=COMMAND+" command not clear, please try again"
	s.sendto(statusMsg1, clientAddr)

##############################################################################

if __name__ == '__main__':			#main function

	port1=commandArg()			#Take port input from command line arguments
	host=""					#Assign available IP 
	port=int(port1)				#Convert port information to int type
	if port < 5000:				#Ports should only be selected greated than 5000 else error will be raised
		print("Enter port number greater than 5000")
		sys.exit()
	
		
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#Socket definition for UDP protocol
	s.bind((host, port)) 					#Socket binding using host and IP address
	print "waiting on port:", port

	while 1:						#Server socket is always open for communication with client unless client requests to exit
		propMsg, clientAddr=s.recvfrom(1024)		#Receive command information from client
		splitMsg=propMsg.split("???")			#Split the command and message sent by client depending on the delimiter for secure messages
		COMMAND=splitMsg[1]	

	
		if(COMMAND=="list"):				#Select required function depending on command sent by client
	       		listOption(COMMAND, clientAddr)
		elif(COMMAND=="exit"):
       			exitOption()
       		elif(COMMAND==("put")):
			fileI=splitMsg[2]
                	putFi(COMMAND, fileI, clientAddr)
        	elif(COMMAND==("get")):
               		fileI=splitMsg[2]
			getFi(COMMAND, fileI, clientAddr)
		else:
			otherC(COMMAND, clientAddr)

		
