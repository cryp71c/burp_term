#!/usr/bin/env python3

class target():
    def __init__(self, ip: str, port: int, scheme: str):
        self.ip = ip
        self.port = port
        self.scheme = scheme
        self.params = {}
        self.args=""
        self.injections=""
        self.username=""
        self.password=""
        self.proxy=""
        self.user_agent=""

    def show_target_options(self):
        print("ip: %s"% self.ip)
        print("port: %d"% self.port)
        print("scheme: %s"% self.scheme)
        print("params: %s"% self.params)
        print("args: %s"% self.args)
        print("injections: %s"% self.injections)
        print("username: %s"% self.username)
        print("password: %s"% self.password)
        print("proxy: %s"% self.proxy)
        print("proxy: %s"% self.user_agent)

def main():
    tlist = []
    tlist.append(target("192.168.54.254", 4444, "http"))

    tlist[0].show_target_options()

if __name__=="__main__":
    main()