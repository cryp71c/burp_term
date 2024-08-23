#!/usr/bin/env python3
import socket
import requests
import re
from urllib.parse import urlparse

class target():
    def __init__(self, ip: str, port: int, scheme: str, target_id: int):
        self.target_id=target_id
        self.ip = ip
        self.port = port
        self.socket = self.ip+":"+str(self.port)
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
        print("Useragent: %s"% self.user_agent)

class workspace():
    def __init__(self, workspace_id):
        self.name=str(workspace_id)
        self.workspace_id = workspace_id
        self.targets=[]
    
    def workspace_help(self):
        print("Options:")
        print("\tadd\t:\tcreates target, 127.0.0.1:1337 OR http://127.0.0.1:1337/")
        print("\tset\t:\tset <variable> <target_id> <value>")
        print("\trm\t:\tremove target, takes workspace_id")
        print("\tls\t:\tlist targets")
        print("\thelp")
        print("\tback goes back to workspaces\n")

    def interact(self):
        print("Past Compile")
        tid = 0
        cmds = ["add", "set", "rm", "ls", "help", "exit", "back"]
        print(f"[*] Welcome to interactive mode!")
        self.workspace_help()
        while True:
            user_input=""
            cmd=""
            user_input = input(f"workspace{self.workspace_id}::>>")
            cmd = user_input.split(" ")
            if cmd[0] in cmds:
                if cmd[0] == "add":
                    if "//" not in cmd [1]:
                        cmd[1]="//"+cmd[1]
                    t = urlparse(cmd[1])
                    if t:
                        try:
                            p = t.netloc.split(":")[1] if ':' in t.netloc else socket.getservbyname(t.scheme)
                        except OSError:
                            print(f"[*] Unrecognized port for scheme translation {t.netloc.split(':')[1]}.. Just a warning, continuing...")
                            continue
                        self.targets.append(target(ip=t.netloc.split(':')[0], port=p, scheme=t.scheme, target_id=tid))
                        print(f"[+] Successfully aded target {self.targets[tid].scheme}{self.targets[tid].socket}")
                        tid+=1
                    else:
                       print(f"Invalid target: {cmd[0]}")
                if cmd[0] == "set":
                    pass
                if cmd[0] == "rm":
                    pass
                if cmd[0] == "ls":
                    for i in self.targets:
                        print(f"{self.targets.index(i)}) {i.ip}:{i.port}")
                if cmd[0] == "help":
                    pass
                if cmd[0] == "back":
                    print("In back")
                    return
            
def main_help():
    print("Options:")
    print("\tcreate\t:\tcreates workspaces, auto increments id")
    print("\tset\t:\tset workspace, takes workspace_id")
    print("\trm\t:\tremove workspaces, takes workspace_id")
    print("\tls\t:\tlist workspaces")
    print("\thelp")
    print("\texit\n")

def main():
    cmds = ["create", "set", "rm", "ls", "help", "exit"]
    wsid = 0 # Start workspace id's at 0
    workspaces=[]
    workspaces.append(workspace(wsid))
    wsid+=1
    print("[+] Created default workspace @ id 0\n")
    main_help()
    while True:
        user_input = input("burp_term::>>").lower()
        cmd = user_input.split(' ')
        if cmd[0] in cmds:
            if cmd[0] == "create":
                workspaces.append(workspace(wsid))
                wsid+=1
            elif cmd[0] == "set":
                if len(cmd) == 2:
                    workspaces[int(cmd[1])].interact()
                    cmd = ""
                elif len(cmd) > 2:
                    raise OverflowError(f"[!] Too many arguments!")
                    continue
                else:
                    raise ValueError(f"[!] Too little arguments!")
                    continue
            elif cmd[0] == "rm":
                if len(cmd) == 2:
                    workspaces.pop(int(cmd[1]))
                elif len(cmd) > 2:
                    raise OverflowError(f"[!] Too many arguments!")
                    continue
                else:
                    raise ValueError(f"[!] Too little arguments!")
                    continue
            elif cmd[0] == "ls":
                for i in workspaces:
                    print(f"{workspaces.index(i)}) {i.name}")
            elif cmd[0] == "help":
                main_help()
            elif cmd[0] == "exit":
                exit()
                
        else:
            raise TypeError("[!] Invalid command: %s"%user_input)
            continue


if __name__=="__main__":
    main()