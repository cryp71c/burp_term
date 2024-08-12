#!/usr/bin/env python3
import requests
import urllib3
import os
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

try:
	shell = os.getenv("SHELL")
	user = os.getenv("USER")
	pwd = os.getenv("PWD")
except:
	print("Are you in linux?")

session  = requests.Session()

def get_random_ua():
	software_names = [SoftwareName.CHROME.value]
	operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
	user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
	user_agent_rotator.get_random_user_agent()
	user_agent = user_agent_rotator.get_random_user_agent()
	return user_agent

def set_proxy(userin):
	session.proxies.update(f"http://{userin}")

def sqli_help():
	print("sqli help:\n")
	print("\tset post file /path/to/post/file")
	print("\tshow opts/options")
	print("\tset params param1=2&param2=3")

def sqli_menu():
	sqli_help()
	opts = post_parse()
	#opts[0]

def http_req_parse():
	print("Paste your post request below to end paste <enter>EOF:\n")
	lines = []
	while True:
		line = input()
		if line in ["EOF", "EOf", "EoF", "eOF", "Eof", "eof", "eoF"]:
			break
		lines.append(line)
	return lines

def main_help():
	print(f"The usage of burp_term.py is similar to metasploit.")
	print("You can use burp proxy as well!")
	print("\tuse sqli")
	print("\tset proxy 127.0.0.1:8080")

def main():
	print(f"Welcome {user} to BurpTerm!")
	main_help()
	while True:
		uin = input(f"{user}::>").lower()
		if uin == "exit":
			break
		parser = uin.split(" ")
		if parser[0] == "set":
			if parser[1] == "proxy":
				if ":" in parser[2]:
					socket = parser[2]
					if int(parser[2].split(":")[1]) > 65535:
						print(f"Invalid Port number {int(parser[2].split(":")[1])}")
						
				

	#sqli_menu()
		
# GET / HTTP/1.1
# Host: example.org
# User-Agent: user_agent_rotator.get_user_agent()
# Accept: */*
# Connection: keep-alive


	
if __name__== '__main__':
	main()
