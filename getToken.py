import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

def getAuthToken():
    username = input("Please enter your username: ")
    password = getpass("Please enter your password: ")
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    response = requests.post(url, auth=HTTPBasicAuth(username, password))
    token = response.json()['Token']
    print("Token Retrieved: {}".format(token))
    return token
