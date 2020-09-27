import socket


def main():

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = input("请输入服务器ip：")
    server_port = int(input("请输入服务器端口："))
    serverAddress = (server_ip, server_port)
    tcp.connect(serverAddress)

    while True:
        send_data = input("请输入要发送的数据")
        if "exit" in send_data:
            break
        tcp.send(send_data.encode("gbk"))

    tcp.close()


if __name__ == "__main__":
    main()