#!/usr/bin/env python3
import socket
import requests

class target():
    def __init__(self, ip: str, port: int, scheme: str, target_id: int):
        self.target_id=target_id
        self.ip = ip
        self.port = port
        self.socket = self.ip+":"+self.port
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
        print("\tset\t:\tset workspace, takes workspace_id")
        print("\trm\t:\tremove workspaces, takes workspace_id")
        print("\tls\t:\tlist workspaces")
        print("\thelp")
        print("\tback goes back to workspaces\n")
        print("[*] Default workspace session id is 0\n")

    # def import_target_list(path: str):
    #     with open(path, 'r') as file:
    #         for i in file:
    #             if '://' in i:
    #                 tmp = i.split("://")

    #                 # TODO
    #                 #socket.getservbyname(tmp[0])
    #                 # then get the port if there is one, if not set default
    #     file.close()

    def interact(self):
        # (?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])
        # ((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?):([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])
        # ([a-z][a-z0-9+\-.]*)://((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?):([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])
        # (([a-z][a-z0-9+\-.]*)://)?((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?):([1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])
        tid = 0
        cmds = ["add", "set", "rm", "ls", "help", "exit"]
        print(f"[*] Welcome to interactive mode!")
        self.workspace_help()
        while True:
            user_input = input("workspace::>>")
            if cmd[0] in cmds:
                if cmd[0] == "add":
                    
                    self.targets.append(target)
                elif cmd[0] == "set":
                    pass
                elif cmd[0] == "rm":
                    pass
                elif cmd[0] == "ls":
                    pass
                elif cmd[0] == "help":
                    pass
                elif cmd[0] == "back":
                    pass



def main_help():
    print("Options:")
    print("\tcreate\t:\tcreates workspaces, auto increments id")
    print("\tset\t:\tset workspace, takes workspace_id")
    print("\trm\t:\tremove workspaces, takes workspace_id")
    print("\tls\t:\tlist workspaces")
    print("\thelp")
    print("\texit\n")
    print("[*] Default workspace session id is 0\n")

def main():
    cmds = ["create", "set", "rm", "ls", "help", "exit"]
    wsid = 0 # Start workspace id's at 0
    workspaces=[]
    workspaces.append(workspace(wsid))
    wsid+=1
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