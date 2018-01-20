# Chat-application-between-a-Client-and-a-Server-using-Sockets
Socket programming using Python to transfer content and messages between a Client and a Server using Sockets

1.	Requirements: 
a.	Server code (server.py)
b.	Server Port
c.	Client code (client.py)
d.	Client IP address and port
e.	Foo1.txt - Small text to test
f.	Foo2.jpg - Small Image to test
g.	Foo3.txt - Large text to test
h.	Python 2.7


2.	Procedure:
a.	I am using python 2.7 to execute this program.
b.	Define socket with properties according to UDP protocol.
c.	Display menu of commands to user for server and client communication.
d.	Request user to select commands depending on menu displayed.
e.	If user selects Put command
i.	Client will send put command to server
ii.	Server will check the command
iii.	Depending on the file to be transferred, transfer the file to server if the mentioned file is available and store at server location else error out and display error to user as file is not available.
f.	If user selects List command
i.	Client will send list command to server
ii.	Server will check the command
iii.	Server will send all the files to client.
g.	If user selects Get command
i.	Client will send list command to server
ii.	Server will check the command
iii.	Depending on file request by client, server will transfer the file to client and store in client as received_file_name. extension else if the file is not present, server will display error on client side.
h.	If user selects Exit command
i.	Client will send exit command to server
ii.	Server will check the command
iii.	Server will gracefully exit and then client will also quit.


3.	Code:
a.	Client Program
i.	Importing Packages 
 
I am importing external packages to implement command line arguments, file handling and socket programming.

ii.	Taking input using command line arguments
 
Here I am using command line arguments in client program to take input of IP address and port. Here the length of arguments is used to check if user is providing both IP address and port details. If user provides either IP or port or none, then this function will error out.

iii.	Put Function:

 

When the user selects, put[file_name] as input from the menu, client will select file as specified by the user and check if the file exists in the current directory using os.path.isfile and later opens the file to extract the contents. 
The message to be delivered to server is created using the command selected by the user and file contents in binary format, and delimited using delimiter as "???". 
The message is then sent to server to store at in the server location. Server will send acknowledgement for the message received. I am enclosing the Put function in try to catch any exceptions and prevent program abruptly exiting. I am catching the exception in the end of put function.
Once file operation is completed, file is closed using file1.close().
I am using s.settimeout to regularly check if server responds to the client and this will prevent the client getting stuck in loop.

iv.	Get Function

 

When the user selects get[file_name], client will execute getFi function and it will send the command encoded with file name to server. 
I am using s.settimeout to regularly check if server responds to the client and this will prevent the client getting stuck in loop.
Client will then receive packets from server and then write the contents to a file already open in append, binary mode.
Whenever client receives packets from server, it will append the latest contents to the file and close the file.
Once the server sends the final packet, it will also send "done" to indicate end of transmission, the client will then complete the transfer operation and close the file and loop.
I am enclosing the get function in try to catch any exceptions and prevent program abruptly exiting. I am catching the exception in the end of put function.

v.	List function:
 

When user selects list command, the client will send command list to server, requesting to display the contents of server.
Server will then send the contents of it directory to client, which the client will receive and display in client window.
	I am enclosing the get function in try to catch any exceptions and prevent program abruptly exiting. I am catching the exception in the end of put function.
I am using s.settimeout to regularly check if server responds to the client and this will prevent the client getting stuck in loop.

vi.	Exit Function:
	 
	
When the user selects exit option from the menu, the client will then send exit command to server, the server will then gracefully exit. I also made the client exit whenever the server exits.

vii.	Other Commands Function:
	 
When the user selects or enters any other input other than the menu displayed, the client program will error out and display error asking user to re-enter and enter only as per the menu selected.

viii.	Main Function:
 
	
	
	Main menu contains all the calling commands to various functions.
Main menu has socket definition, port assignment and code to select various functions as needed.

S=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

This is used to define UDP socket. This code is enclosed in try and except block to catch socket.error exception.

Main function also has the menu to be displayed to user. User will be given options or commands to select. Depending on the input from the user, main function has if blocks to direct the user input and call the respective functions. For example, if user selects put command menu option, then if block of put function will be selected and put function will be called for execution. This way the entire program is controlled by the main function. Once the function execution is complete, the control is returned back to the main function.

b.	Server Program:

i.	Importing Packages 
 
I am importing external packages to implement command line arguments, file handling and socket programming.

ii.	Taking input using command line arguments
 
Here I am using command line arguments in client program to take input of IP address and port. Here the length of arguments is used to check if user is providing both IP address and port details. If user provides either IP or port or none, then this function will error out.

iii.	Put Function:

 

When the user selects, put[file_name] as input from the menu, client will send the file contents and command as encoded message delimited using "???". 
The encoded message is received by server is later extracted using split and delimiter as "???". Server will then open file with file name sent by the client and write the extracted contents to the file using append, binary mode.
Server will close the file after file operation is completed. Once file operation is completed, file is closed using file1.close(). Server will send acknowledgement back to the client indicating the file is received.


iv.	Get Function

 

When the user selects get[file_name], client will send the file name and command to the user encoded using delimiter. Server will extract the filename and command, verify the command and later send the file back as requested.
Server will send the file as packet back to the user and for each packet sent, it will receive acknowledgement from the client to indicate success. Once the complete data is sent by the server, server will also send "done" to indicate completion of file transfer. This indication is used by the client to be in sync with the server,
Once the file transfer is complete, server will close the file opened.
Initially, server will check if the file specified by the use is present in the current directory or not, if file not present, server will send an error message back to the client.

v.	List function:
 

When user selects list command, the client will send command list to server, requesting to display the contents of server.
Server will then send the contents of it directory to client, which the client will receive and display in client window. 
Server will first read the contents of current directory and append the files to the list. Once the list is ready, server will then create a string of all the list contents as we can only send string using send.to().
Server will then send the contents of folder to client, the client will then acknowledge the reception.
	

vi.	Exit Function:
	 
	
When the user selects exit option from the menu, the client will then send exit command to server, the server will then gracefully exit. I also made the client exit whenever the server exits.

vii.	Other Commands Function:
 
	
When the user selects or enters any other input other than the menu displayed, the client program will error out and display error asking user to re-enter and enter only as per the menu selected.

viii.	Main Function:
 
	
	
	Main menu contains all the calling commands to various functions.
Main menu has socket definition, port assignment and code to select various functions as needed.

S=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

This is used to define UDP socket. This code is enclosed in try and except block to catch socket.error exception.

Main function also has the menu to be displayed to user. User will be given options or commands to select. Depending on the input from the user, main function has if blocks to direct the user input and call the respective functions. For example, if user selects put command menu option, then if block of put function will be selected and put function will be called for execution. This way the entire program is controlled by the main function. Once the function execution is complete, the control is returned back to the main function.
