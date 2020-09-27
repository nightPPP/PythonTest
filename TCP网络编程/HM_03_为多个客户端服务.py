import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 7890))

    tcp_server_socket.listen(128)

    while True:

        print("------1-----------")
        # 客户端传过来的数据，没接收到就不会向下执行
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("----------2----------")
        print(client_addr)

        # 当拿到客户端的数据才会走下来
        while True:

            rcv_data = new_client_socket.recv(1024)
            print(rcv_data)
            # rcv_data有数据的时候
            if rcv_data:
                new_client_socket.send("haha".encode("utf-8"))
            else:
                break

        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
