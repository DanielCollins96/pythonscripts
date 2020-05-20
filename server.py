#!/usr/bin/env python

class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
    def ping(self, ip_addr):
        print("Pinging the server")

if __name__ == '__main__':
    server = Server('192.168.1.20', 'hi')
    server.ping('192.168.1.20')