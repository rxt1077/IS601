import requests
import pprint
import re

class IRacing:
    pp = pprint.PrettyPrinter(indent=4)
    session = requests.Session()

    def print_cookies(self):
        """Pretty prints the cookies in the current session"""
        print("Current cookies:")
        self.pp.pprint(self.session.cookies.get_dict())

    def get(self, url):
        """Wrapper around GET requests to use session and print info"""
        print(f"GET {url}")
        response = self.session.get(url)
        print(f"STATUS {response.status_code}")
        self.print_cookies()
        return response

    def post(self, url, data):
        """Wrapper around POST requests to use session and print info"""
        print(f"POST {url}")
        print("data:")
        self.pp.pprint(data)
        response = self.session.post(url, data=data)
        print(f"STATUS {response.status_code}")
        self.print_cookies()
        return response

    def __init__(self, username, password):
        """Logs in to iRacing.com and sets up session"""

        # load the login page to get an XSESSIONID cookie
        self.get('https://members.iracing.com/membersite/login.jsp')
        
        # POST username and password
        response = self.post('https://members.iracing.com/membersite/Login',
            data = {
                'username': username,
                'password': password,
                'utcoffset': '240',
                'todaysdate': '',
            }
        )

        # get the driver identity
        result = re.search('customerid=([0-9]+)&', response.text)
        self.driver_id = result.group(1)
