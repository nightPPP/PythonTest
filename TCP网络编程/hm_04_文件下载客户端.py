import socket

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = input("请输入ip---")
    port = int(input("请输入端口号---"))
    addr = (ip, port)

    tcp_socket.connect(addr)

    down_file_name = input("输入要下载的文件名")

    tcp_socket.send(down_file_name.encode("utf-8"))

    recv_data = tcp_socket.recv(1024)

    with open("新" + down_file_name , "wb") as f:
        f.write(recv_data)

    tcp_socket.close()

if __name__ == "__main__":
    main()