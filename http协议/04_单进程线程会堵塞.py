import socket


def service_client(new_socket):
    # 为这个客户端返回数据

    # 接收浏览器发过来的请求，http请求
    request = new_socket.recv(1024)
    print(request)

    # 返回http格式的数据给浏览器
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    response += "<h1>hahaha</h1>"
    new_socket.send(response.encode("utf-8"))
    new_socket.close()


def main():
    # 1创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2绑定
    tcp_server.bind(("", 7890))
    # 3监听
    tcp_server.listen(128)

    tcp_server.setblocking(False)
    client_socket_list = list()

    while True:
        try:
            new_socket, new_addr =  tcp_server.accept()
        except Exception as ret:
            
            print("----没有新的客户端到来---")
        else:
            print("---只要没有产生异常，就说明来了新的客户端---")
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                client_socket.recv()
            except Exception as ret:
                print("---这个客户端没有发送过来数据---")
            else:
                print("---客户端发过来了数据---")

    tcp_server.close()


if __name__ == '__main__':
    main()