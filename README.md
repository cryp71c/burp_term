# burp_term

[!WARNING]  
This script is provided for educational and lawful purposes only. The author is not responsible for any misuse or illegal activities carried out with this tool. Users are required to ensure they have explicit permission and signed consent from the target party before executing this script. Always operate within the boundaries of the law and ethical standards.

`burp_term` is a Python-based tool designed to automate HTTP requests for SQL injection and brute-forcing attacks, with added functionality to manage targets and workspaces interactively.

## Recent Changes
- **New Module:** `httpBrute.py` added for web brute-forcing.
- **Improved Core Logic:** `burp_term.py` refined for better target handling and error management.

## Features
- Organize and manage multiple targets via **workspaces**.
- Perform SQL injections and web brute-force attacks with **automated HTTP requests**.
- Interactive command-line operations for workspace management.

## Installation
```bash
git clone https://github.com/cryp71c/burp_term.git
cd burp_term
python3 -m pip install -r requirements.txt
```

## Modules
### httpBrute.py
This module contains the httpBrute force class as well as an SQLi class. 
Eventually both of these will be able to be run independently using the following syntax:
```bash
python3 burp_term.py -m httpBrute -u http://127.0.0.1:8080/admin/index.php -U /path/to/user/file -P /path/to/pass/file --param "username=^USER^&password=^PASSWORD^"
python3 burp_term.py -m SQLi -u http://127.0.0.1:8080/admin/index.php --param "username=^INJ^&password=fakepass"
```
I really liked, hydra's and burpsuites inject syntax, but for me they felt too slow, I will also allow the printing of content length, and response codes.

## Usage
Run the tool interactively:
```bash
python3 burp_term.py
```
