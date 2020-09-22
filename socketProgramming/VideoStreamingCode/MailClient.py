from socket import *
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailhost = "smtp.163.com"#Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
serverPort=25
myemail="liukunlin395@163.com"
mypassword="LSJUEEGDRQHGDBGG"
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailhost,serverPort))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# login
# Fill in start
msgLogin="auth login\r\n"
clientSocket.send(msgLogin.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if(recv8[:3] != '334'):
    print("login failed")
clientSocket.send(base64.b64encode(myemail.encode())+b'\r\n')
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if(recv2[:3] != '334'):
    print("accout login failed")
clientSocket.send(base64.b64encode(mypassword.encode())+b'\r\n')
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if(recv3[:3] != '235'):
    print("password login failed")
# Fill in end
# Send MAIL FROM command and print server response.
# Fill in start
msgFrom="Mail from:"+"<"+myemail+">"+"\r\n"
clientSocket.send(msgFrom.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if(recv4[:3] != '250'):
    print("command mail from failed")
# Fill in end
# Send RCPT TO command and print server response. 
# Fill in start
msgTo="RCPT TO:"+"<"+myemail+">"+"\r\n"
clientSocket.send(msgTo.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if(recv5[:3] != '250'):
    print("command mail from failed")
# Fill in end
# Send DATA command and print server response. 
# Fill in start
msgData="Data\r\n"
clientSocket.send(msgData.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if(recv6[:3] != '354'):
    print("command data failed")
# Fill in end
# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if(recv7[:3] != '250'):
    print("message transport failed")
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitcommand="QUIT\r\n"
clientSocket.send(quitcommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if(recv7[:3] != '221'):
    print("command quit failed")
# Fill in end