import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass
from pprint import pprint

# Collect user information
username = input("Please enter your username: ")
password = getpass("Please enter your password: ")

# DevNet Sandbox URL's
baseURL = 'https://sandboxdnac.cisco.com'
authAPI = '/dna/system/api/v1/auth/token'
devLsAPI = '/dna/intent/api/v1/network-device'

# Create variables for parameters and headers
authPayload = {}
authHead = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Variable for URL for authentication token
dnaAuth = baseURL + authAPI

# Request token
authResponse = requests.post(dnaAuth, auth=HTTPBasicAuth(username, password), headers=authHead, data=authPayload)

TOKEN = authResponse.json()['Token']

#Variable for URL for get devices request
dnaDevLs = baseURL + devLsAPI

# Create varialbes for parameters and headers
getPayload={}
getHead = {
        'X-Auth-Token': TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

# Get devices list from DNA sandbox
getResp = requests.get(dnaDevLs, headers=getHead, data=getPayload)

devices = getResp.json()

pprint("Devices found: {} \n" + devices)
