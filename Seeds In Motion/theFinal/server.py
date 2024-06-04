import socket
from _thread import *

server = "192.168.11.105"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)  
print("Waiting for a connection, Server Started")

def read_pos(str):
    return tuple(map(int, str.split(",")))


def make_pos(tup):
    return ",".join(map(str, tup))


player_positions = [(0,0), (100,100)]
box_positions = [(50,50), (150,150)]  

def threaded_client(conn, player):
   
    conn.send(str.encode(make_pos(player_positions[player]) + "|" + "|".join(map(make_pos, box_positions))))
    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break

            data = data.split("|")
            player_positions[player] = read_pos(data[0])
            box_positions[:] = map(read_pos, data[1:])

            if player == 1:
                reply = make_pos(player_positions[0])
            else:
                reply = make_pos(player_positions[1])

            reply += "|" + "|".join(map(make_pos, box_positions))
            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer = 1 - currentPlayer  