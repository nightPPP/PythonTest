import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    localAddr = ("192.168.0.12", 8080)
    udp_socket.bind(localAddr)

    while True:
        receiveData = udp_socket.recvfrom(2048)
        msg = receiveData[0]
        ip = receiveData[1]
        strmsg = bytes.decode(msg)
        print(type(strmsg))
        if "exit" == strmsg:
            break

        print("ip--%s , msg--%s" %(ip, strmsg))

    udp_socket.close()


if __name__ == "__main__":
    main()
