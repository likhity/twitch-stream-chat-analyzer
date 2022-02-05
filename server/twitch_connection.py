import socket

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'likhity'
token = "oauth:e8dbow1jybxddssj9778q5ne9r32lx"
channel = '#cohhcarnage'

twitchChatConnection = socket.socket()

twitchChatConnection.connect((server, port))

twitchChatConnection.send(f"PASS {token}\n".encode('utf-8'))
twitchChatConnection.send(f"NICK {nickname}\n".encode('utf-8'))
twitchChatConnection.send(f"JOIN {channel}\n".encode('utf-8'))

resp = twitchChatConnection.recv(2048).decode('utf-8')

while(True):
  resp = twitchChatConnection.recv(2048).decode('utf-8')
  resp = resp.split(":")[2]
  print(resp)