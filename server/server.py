
import socket

server = 'irc.chat.twitch.tv'
port = 6697
nickname = 'likhity'
token = "oauth:e8dbow1jybxddssj9778q5ne9r32lx"
channel = '#ninja'

sock = socket.socket()

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')

resp

sock.close()