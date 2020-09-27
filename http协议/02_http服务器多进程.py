import multiprocessing
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

    while True:

        # 4等待新客户端的链接
        new_socket, client_addr = tcp_server.accept()

        process = multiprocessing.Process(target=service_client, args=(new_socket,))
        process.start()
        new_socket.close()

        # 5为这个客户端服务
        # service_client(new_socket)

    tcp_server.close()


if __name__ == '__main__':
    main()