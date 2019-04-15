# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:49:44 2019

@author: Matthew DeCarlo
"""

# Import socket module 
import socket                
  



    
  
# Define the port on which you want to connect 
port = input("Enter Port number to destination server(Default is 1200):")
if port == '':
    port = 1200
else:    
    port = int(port)               
serverIP = input("Enter ServerIP(Default is 127.0.0.1):")
if serverIP == '':
    serverIP = '127.0.0.1'


#send  and collect palindrome
flag = 1
while flag == 1:  
    # Create a socket object 
    s = socket.socket()      
    # connect to the server on local computer 
    try:
        s.connect((serverIP, port)) 
        x = input("Test A Palindrome:")
        #if null, terminate
        if x == '':
            print("GoodBye")
            flag = 0
            break
        #send data to server
        s.sendall(str.encode(x))  
        # receive data from the server 
        #sends maximum of 1024 bytes
        print((s.recv(1024).decode())) 
        # close the connection 
        s.close()
    except:
        print("Something went wrong when connecting to the server")
        flag = 0