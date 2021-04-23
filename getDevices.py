import requests
import getToken

def getDevice():
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    token = getToken()
    payload={}
    headers = {
        'X-Auth-Token': token,
        'Accept': 'application/json'
    }
    resp = requests.request("GET", url, headers=headers, data=payload)
    device = resp.json()['response']
    print("Devices found: {}".format(device))
