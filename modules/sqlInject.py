import requests
import mimetypes
from requests.exceptions import ConnectionError

class sqlinject:
    def __init__(self, scheme, ip, port, payload, 
                 login_path, user, user_file, password, 
                 password_file, user_agent, mimetype='text/plain', 
                 proxy={'http':'http://127.0.0.1:8080'}):

        self.url = str(scheme)+str(ip)+str(port)
        self.payload = payload
        self.login_path = login_path
        self.user_agent = user_agent
        self.mimetype = mimetype
        self.proxy = proxy
        self.user = user
        self.password = password
        self.user_file = user_file
        self.password_file = password_file
        self.session = requests.Session()
        self.headers = {'Content-Type': {self.mimetype}}
        
    def inject():
        pass