import socket


def main():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.bind(("", 7890))

    tcp_socket.listen(128)

    new_client_socket, new_socket_add = tcp_socket.accept()

    print("--------1-------")
    file_name = new_client_socket.recv(1024)
    print("--------2-------")
    new_client_socket.send("sssssssss".encode("utf-8"))

    new_client_socket.close()
    tcp_socket.close()


if __name__ == "__main__":
    main()
