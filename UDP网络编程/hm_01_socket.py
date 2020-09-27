import socket


def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bstr = "顶顶顶顶".encode(encoding="utf-8")
    udp_socket.sendto("顶顶顶顶".encode("utf-8"), ("192.168.0.12", 8080))
    # print(type(bstr))
    udp_socket.close()


if __name__ == "__main__":
    main()