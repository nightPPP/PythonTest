import socket


def send_msg(udp_socket):
    udp_socket.sendto("顶顶顶顶".encode("utf-8"), ("192.168.0.13", 8080))
    print("发送成功")


def receive(udp_socket):
    receiveData = udp_socket.recvfrom(2048)
    msg = receiveData[0]
    ip = receiveData[1]
    strmsg = bytes.decode(msg)

    print("ip--%s , msg--%s" % (ip, strmsg))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    localAddr = ("192.168.0.12", 8080)
    udp_socket.bind(localAddr)

    while True:

        op = input("请输入功能编号：")
        if "1" == op:
            send_msg(udp_socket)
        elif "2" == op:
            receive(udp_socket)
        elif "0" == op:
            break
        else:
            print("输入有误")

    udp_socket.close()


if __name__ == "__main__":
    main()
