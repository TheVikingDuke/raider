import socket

target_host = "localhost"
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Note. no connection like tcp
client.sendto(b"AAABBBCCC",(target_host, target_port))

data, addr = client.recvfrom(4096)

print(Data)
print(data.decode())
print(addr)

client.close()
