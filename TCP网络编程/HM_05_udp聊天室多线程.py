import socket
import threading


def rec_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, ip, port):
    while True:
        send_data = input("请输入要发送的数据 ：")
        udp_socket.sendto(send_data.encode("utf-8"), (ip, port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("", 7890))

    ip = input("请输入对方的ip：")
    port = int(input("请输入对方的端口号："))

    tRec = threading.Thread(target=rec_msg, args=(udp_socket,))

    tSend = threading.Thread(target=send_msg, args=(udp_socket, ip, port,))

    tRec.start()
    tSend.start()


if __name__ == "__main__":
    main()