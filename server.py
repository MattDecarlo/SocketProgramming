# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:49:58 2019

@author: Matthew DeCarlo
"""
import socket
from threading import Thread
def isPalindrome(temp):
    #Tests string if its palindrom or not,
    #Will return string of palindrome or not palindrome
    #Converts all characters to uppercase So the checker isnt case sensitive
    #print(temp)
    temp = str(temp)
    temp = temp.upper()
   # print(type(temp))
    temp = list(temp)
    #print(temp)
    rev_temp = temp
    rev_temp = list(reversed(rev_temp))
    #print(type(rev_temp))
    if temp == rev_temp:
        return " Palindrome "
    else:
        return " Not Palindrome "
        

s1 = socket.socket()
#s2 = socket.socket()
print("Socket Created")
port = input("Enter Port number to this server(Default is 1200):")
print(port)
if port == '':
    port = 1200
else:    
    port = int(port)   
#binds the socket to the ip address of the local machine, and the port number that was inputed on start of server
try:    
    s1.bind(('', port))
except:
    print("Socket already binded on that port or something terrible wrong")
    
#Sets the server socket into listening mode
s1.listen(5)

print('Socket Listening')


def thread1():
    #This loop allows the server to recieve data, and return the checked palindrome data to the client
    while True:
        conn, addr = s1.accept()
        print('s1:got connection from', addr)
        data = conn.recv(1024)
        if not data:
            break
        answer = isPalindrome(data.decode())
        print(data.decode()+" Is"+answer)
        conn.sendall(answer.encode())
        conn.close()
def thread2():
    while True:
        conn, addr = s1.accept()
        print('s2:got connection from', addr)
        #Recieves 1024 bytes 
        data = conn.recv(1024)
        if not data:
            break
        answer = isPalindrome(data.decode())
        print(data.decode()+" Is"+answer)
        conn.sendall(answer.encode())
        conn.close() 
        
#for multithreading allowing multiple users(can only have a max of 2 users)
if __name__ == '__main__':
    Thread(target = thread1).start()
    Thread(target = thread2).start()   