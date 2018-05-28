# -*- coding: utf-8 -*-
import socket


def create_tun_interface():
    from pytun import TunTapDevice

    tun1 = TunTapDevice(name="gtw")
    tun1.addr = '192.168.13.10'
    tun1.persist(True)
    tun2 = TunTapDevice(name='tun_socket')
    tun2.addr = '192.168.13.1'
    tun2.persist(True)

    server_program(tun2.addr)


def server_program(tun):

    PORT = 999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((tun, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.send("PING IS OK!")
	print(data)

    conn.close()

if __name__ == '__main__':
    create_tun_interface()